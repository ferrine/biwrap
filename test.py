import biwrap


@biwrap.biwrap
def hiwrap(fn, hi=True):
    def new(*args, **kwargs):
        if hi:
            print('hi')
        else:
            print('bye')
        return fn(*args, **kwargs)
    return new


def test_wrapped1(capsys):
    @hiwrap
    def fn(n):
        print(n)
    fn(1)
    captured = capsys.readouterr()
    assert captured.out == "hi\n1\n"


def test_wrapped2(capsys):
    @hiwrap(hi=False)
    def fn(n):
        print(n)

    fn(1)
    captured = capsys.readouterr()
    assert captured.out == "bye\n1\n"


def test_wrapped3(capsys):
    class O:
        @hiwrap(hi=False)
        def fn(self, n):
            print(n)

    O().fn(1)
    captured = capsys.readouterr()
    assert captured.out == "bye\n1\n"


def test_wrapped4(capsys):
    class O:
        @hiwrap
        def fn(self, n):
            print(n)

    O().fn(1)
    captured = capsys.readouterr()
    assert captured.out == "hi\n1\n"


def test_wrapped5(capsys):
    class O:
        @classmethod
        @hiwrap
        def fn(cls, n):
            print(n)

    O.fn(1)
    captured = capsys.readouterr()
    assert captured.out == "hi\n1\n"


def test_wrapped6(capsys):
    class O:
        @classmethod
        @hiwrap(hi=False)
        def fn(cls, n):
            print(n)

    O.fn(1)
    captured = capsys.readouterr()
    assert captured.out == "bye\n1\n"


def test_wrapped7(capsys):

    def fn(n):
        print(n)

    fn = hiwrap(fn, hi=False)
    fn(1)
    captured = capsys.readouterr()
    assert captured.out == "bye\n1\n"


def test_wrapped8(capsys):
    class O:
        def __init__(self, n):
            self.n = n

        @property
        @hiwrap
        def fn(self):
            return self.n

    num = O(1).fn
    print(num)
    captured = capsys.readouterr()
    assert captured.out == "hi\n1\n"


def test_wrapped9(capsys):
    class W:
        def __init__(self, n):
            self.n = n

        @biwrap.biwrap
        def wrap(self, fn, text='hi'):
            def wrapped(*args, **kwargs):
                for _ in range(self.n):
                    print(text)
                return fn(*args, **kwargs)
            return wrapped

    wr = W(3)

    @wr.wrap
    def fn(n):
        print(n)

    fn(1)

    @wr.wrap(text='bye')
    def fn(n):
        print(n)

    wr.n = 2
    fn(2)
    captured = capsys.readouterr()
    assert captured.out == "hi\nhi\nhi\n1\nbye\nbye\n2\n"



import functools
import inspect

__all__ = [
    'biwrap'
]


def biwrap(wrapper):
    if inspect.ismethod(wrapper):
        @functools.wraps(wrapper)
        def enhanced(self, *args, **kwargs):
            if len(args) > 0:
                newfn = wrapper(self, *args, **kwargs)
                return newfn
            else:
                newwrapper = functools.partial(wrapper, self, **kwargs)
                return newwrapper
    else:
        @functools.wraps(wrapper)
        def enhanced(*args, **kwargs):
            if len(args) > 0:
                newfn = wrapper(*args, **kwargs)
                return newfn
            else:
                newwrapper = functools.partial(wrapper, **kwargs)
                return newwrapper
    return enhanced

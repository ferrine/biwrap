# biwrap
Yet simple util to make wrapper with optional arguments

## Installation
Master branch
```
pip install git+https://github.com/ferrine/biwrap
```
Latest release
```
pip install biwrap
```

## Overview
Some wrappers may have optional arguments and we often want to avoid `@wrapper()` calls and use `@wrapper` instead

This works for simple wrapper
```python
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
```

Defined wrapper can be used in both ways

```python
@hiwrap
def fn(n):
    print(n)
fn(1)
#> hi
#> 1

@hiwrap(hi=False)
def fn(n):
    print(n)
fn(1)
#> bye
#> 1
```

`biwrap` also works for bound methods

```python
class O:
    @hiwrap(hi=False)
    def fn(self, n):
        print(n)

O().fn(1)
#> bye
#> 1
```

Class methods / properties are supported too
```python
class O:
    def __init__(self, n):
        self.n = n

    @classmethod
    @hiwrap
    def fn(cls, n):
        print(n)
    
    @property
    @hiwrap(hi=False)
    def num(self):
        return self.n
        
        
o = O(2)
o.fn(1)
#> hi
#> 1
print(o.num)
#> bye
#> 2
```

Function like call is OK too

```python
def fn(n):
    print(n)

fn = hiwrap(fn, hi=False)
fn(1)
#> bye
#> 1
```

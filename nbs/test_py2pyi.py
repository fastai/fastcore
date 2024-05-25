__all__ = ['f','g']

from fastcore.meta import delegates
from fastcore.utils import patch

class X(int): pass

def f(a:int, b:str='a')->str:
    "I am f"
    return 1

@delegates(f)
def g(c, d:X, **kwargs)->str:
    "I am g"
    return 2

def j(c:int, d:str='a')->str:
    "I am j"
    return 1

class A:
    @delegates(j)
    def h(self, b:bool=False, **kwargs):
        a = 1
        # A is 1 now!
        return a

class B: ...

@patch
@delegates(j)
def k(self:(A,B), b:bool=False, **kwargs): return 1

@patch
@delegates(j)
def m(self:A, b:bool=False, **kwargs): return 1

@patch
def n(self:A, b:bool=False, **kwargs):
    "No delegates here mmm'k?"
    return 1


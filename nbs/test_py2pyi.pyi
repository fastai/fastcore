__all__ = ['f', 'g']
from fastcore.meta import delegates
from fastcore.utils import patch

class X(int):
    pass

def f(a: int, b: str='a') -> str:
    """I am f"""
    ...

def g(c, d: test_py2pyi.X, *, b: str='a') -> str:
    """I am g"""
    ...

def j(c: int, d: str='a') -> str:
    """I am j"""
    ...

class A:

    def h(self, b: bool=False, *, d: str='a'):
        ...

class B:
    ...

@patch
def k(self: (test_py2pyi.A, test_py2pyi.B), b: bool=False, *, d: str='a'):
    ...

@patch
def m(self: test_py2pyi.A, b: bool=False, *, d: str='a'):
    ...

@patch
def n(self: A, b: bool=False, **kwargs):
    """No delegates here mmm'k?"""
    ...
import numpy as np
import io,operator,sys,os,re,mimetypes,itertools,shutil,pickle,tempfile,subprocess
import itertools,random,inspect,functools,math,bz2,typing,numbers,warnings,threading

from dataclasses import dataclass
from functools import partial,reduce
from threading import Thread
from time import sleep
from copy import copy
from contextlib import redirect_stdout,contextmanager
from collections.abc import Iterable,Iterator,Generator,Collection,Sequence
from types import SimpleNamespace
from pathlib import Path
from collections import defaultdict,Counter
from operator import itemgetter,attrgetter
from uuid import uuid4

# External modules
from numpy import array,ndarray
from pdb import set_trace

#Optional modules
try: import matplotlib.pyplot as plt
except: pass

try:
    from types import WrapperDescriptorType,MethodWrapperType,MethodDescriptorType
except ImportError:
    WrapperDescriptorType = type(object.__init__)
    MethodWrapperType = type(object().__str__)
    MethodDescriptorType = type(str.join)
from types import BuiltinFunctionType,BuiltinMethodType,MethodType,FunctionType

NoneType = type(None)
string_classes = (str,bytes)

def is_iter(o):
    "Test whether `o` can be used in a `for` loop"
    #Rank 0 tensors in PyTorch are not really iterable
    return isinstance(o, (Iterable,Generator)) and getattr(o,'ndim',1)

def is_coll(o):
    "Test whether `o` is a collection (i.e. has a usable `len`)"
    #Rank 0 tensors in PyTorch do not have working `len`
    return hasattr(o, '__len__') and getattr(o,'ndim',1)

def all_equal(a,b):
    "Compares whether `a` and `b` are the same length and have the same contents"
    if not is_iter(b): return False
    return all(equals(a_,b_) for a_,b_ in itertools.zip_longest(a,b))

def noop (x=None, *args, **kwargs):
    "Do nothing"
    return x

def noops(self, x=None, *args, **kwargs):
    "Do nothing (method)"
    return x

def one_is_instance(a, b, t): return isinstance(a,t) or isinstance(b,t)

def equals(a,b):
    "Compares `a` and `b` for equality; supports sublists, tensors and arrays too"
    if one_is_instance(a,b,type): return a==b
    if hasattr(a, '__array_eq__'): return a.__array_eq__(b)
    if hasattr(b, '__array_eq__'): return b.__array_eq__(a)
    cmp = (np.array_equal if one_is_instance(a, b, ndarray       ) else
           operator.eq    if one_is_instance(a, b, (str,dict,set)) else
           all_equal      if is_iter(a) or is_iter(b) else
           operator.eq)
    return cmp(a,b)

from fastcore.parallel import *
from datetime import *
import random
import os

# from contextlib import contextmanager,ExitStack
from multiprocessing import Process, Queue
import concurrent.futures,time
from multiprocessing import Manager

def print_time(i): 
    time.sleep(random.random()/1000)
    print(i, os.getpid(), datetime.now())

class _C:
    def __call__(self, o): return ((i+1) for i in o)

items = range(5)

if __name__ == "__main__":
    parallel(print_time, range(5), n_workers=2, pause=0.25);
    res = list(parallel_gen(_C, items, n_workers=2))
    print(res)
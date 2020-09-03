# Welcome to fastcore
> Python goodies to make your coding faster, easier, and more maintainable


Python is a powerful, dynamic language. Rather than bake everything into the language, it lets the programmer customize it to make it work for them. `fastcore` uses this flexibility to add to Python features inspired by other languages we've loved, like multiple dispatch from Julia, mixins from Ruby, and currying, binding, and more from Haskell. It also adds some "missing features" and clean up some rough edges in the Python standard library, such as simplifying parallel processing, and bringing ideas from NumPy over to Python's `list` type.

## Installing

To install fastcore run: `conda install fastcore` (if you use Anaconda, which we strongly recommend) or `pip install fastcore`. For an [editable install](https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install), clone this repo and run: `pip install -e ".[dev]"`.

## A tour

`fastcore` contains many features. See the [docs](https://fastcore.fast.ai) for all the details, which cover the modules provided:

- `test`: Simple testing functions
- `foundation`: Mixins, delegation, composition, and more
- `utils`: Utility functions to help with functional-style programming, parallel processing, and more
- `dispatch`: Multiple dispatch methods
- `transform`: Pipelines of composed partially reversible transformations

Here's a (somewhat) quick tour of a few higlights, showing examples from each of these modules.

### Documentation

All fast.ai projects, including this one, are built with [nbdev](https://nbdev.fast.ai), which is a full literate programming environment built on Jupyter Notebooks. That means that every piece of documentation, including the page you're reading now, can be accessed as interactive Jupyter notebooks. In fact, you can even grab a link directly to a notebook running interactively on Google Colab - if you want to follow along with this tour, click the link below, or click the badge at the top of the page:

```python
colab_link('index')
```


[Open `index` in Colab](https://colab.research.google.com/github/fastai/fastcore/blob/master/nbs/index.ipynb)


The full docs are available at [fastcore.fast.ai](https://fastcore.fast.ai). The code in the examples and in all fast.ai libraries follow the [fast.ai style guide](https://docs.fast.ai/dev/style.html). In order to support interactive programming, all fast.ai libraries are designed to allow for `import *` to be used safely, particular by ensuring that [`__all__`](https://riptutorial.com/python/example/2894/the---all---special-variable) is defined in all packages. In order to see where a function is from, just type it:

```python
coll_repr
```




    <function fastcore.foundation.coll_repr(c, max_n=10)>



For more details, including a link to the full documentation and source code, use `doc`, which pops up a window with this information:

```python
doc(coll_repr)
```

<img width="499" src="nbs/images/att_00000.png" align="left">

The documentation also contains links to any related functions or classes, which appear like this: `coll_repr` (in the notebook itself you will just see a word with back-ticks around it; the links are auto-generated in the documentation site). The documentation will generally show one or more examples of use, along with any background context necessary to understand them. As you'll see, the examples for each function and method are shown as tests, rather than example outputs, so let's start by explaining that. 

### Testing

fastcore's testing module is designed to work well with [nbdev](https://nbdev.fast.ai), which is a full literate programming environment built on Jupyter Notebooks. That means that your tests, docs, and code all live together in the same notebook. fastcore and nbdev's approach to testing starts with the premise that your all your tests should pass. If one fails, no more tests in a notebook are run.

Tests look like this:

```python
test_eq(coll_repr(range(1000), 5), '(#1000) [0,1,2,3,4...]')
```

That's an example from the docs for `coll_repr`. As you see, it's not showing you the output directly. Here's what that would look like:

```python
coll_repr(range(1000), 5)
```




    '(#1000) [0,1,2,3,4...]'



So, the test is actually showing you what the output looks like, because if the function call didn't return `'(#1000) [0,1,2,3,4...]'`, then the test would have failed.

So every test shown in the docs is also showing you the behavior of the library --- and vice versa!

Test functions always start with `test_`, and then follow with the operation being tested. So `test_eq` tests for equality (as you saw in the example above). This includes tests for equality of arrays and tensors, lists and generators, and many more:

```python
test_eq([0,1,2,3], np.arange(4))
```

When a test fails, it prints out information about what was expected:

```python
test_eq([0,1,2,3], np.arange(3))
```

```
----
  AssertionError: ==:
  [0, 1, 2, 3]
  [0 1 2]
```

If you want to check that objects are the same type, rather than the just contain the same collection, use `test_eq_type`.

You can test with any comparison function using `test`, e.g test whether an object is less than:

```python
test(2, 3, operator.lt)
```

You can even test that exceptions are raised:

```python
def divide_zero(): return 1/0
test_fail(divide_zero)
```

...and test that things are printed to stdout:

```python
test_stdout(lambda: print('hi'), 'hi')
```

### Foundations

fast.ai is unusual in that we often use [mixins](https://en.wikipedia.org/wiki/Mixin) in our code. Mixins are widely used in many programming languages, such as Ruby, but not so much in Python. We use mixins to attach new behavior to existing libraries, or to allow modules to add new behavior to our own classes, such as in extension modules. One useful example of a mixin we define is `Path.ls`, which lists a directory and returns an `L` (an extended list class which we'll discuss shortly):

```python
p = Path('images')
p.ls()
```




    (#6) [Path('images/att_00007.png'),Path('images/att_00000.png'),Path('images/puppy.jpg'),Path('images/att_00006.png'),Path('images/mnist3.png'),Path('images/att_00005.png')]



You can easily add you own mixins with the `patch` [decorator](https://realpython.com/primer-on-python-decorators/), which takes advantage of Python 3 [function annotations](https://www.python.org/dev/peps/pep-3107/#parameters) to say what class to patch:

```python
@patch
def num_items(self:Path): return len(self.ls())

p.num_items()
```




    6



We also use `**kwargs` frequently. In python `**kwargs` in a parameter like means "*put any additional keyword arguments into a dict called `kwargs`*". Normally, using `kwargs` makes an API quite difficult to work with, because it breaks things like tab-completion and popup lists of signatures. `utils` provides `use_kwargs` and `delegates` to avoid this problem. See our [detailed article on delegation](https://www.fast.ai/2019/08/06/delegation/) on this topic.

`GetAttr` solves a similar problem (and is also discussed in the article linked above): it's allows you to use Python's exceptionally useful `__getattr__` magic method, but avoids the problem that normally in Python tab-completion and docs break when using this. For instance, you can see here that Python's `dir` function, which is used to find the attributes of a python object, finds everything inside the `self.default` attribute here:

```python
class Author:
    def __init__(self, name): self.name = name

class ProductPage(GetAttr):
    _default = 'author'
    def __init__(self,author,price,cost): self.author,self.price,self.cost = author,price,cost

p = ProductPage(Author("Jeremy"), 1.50, 0.50)
[o for o in dir(p) if not o.startswith('_')]
```




    ['author', 'cost', 'name', 'price']



Looking at that `ProductPage` example, it's rather verbose and duplicates a lot of attribute names, which can lead to bugs later if you change them only in one place. `fastcore` provides `store_attr` to simplify this common pattern. It also provides `basic_repr` to give simple objects a useful `repr`:

```python
class ProductPage:
    store_attrs = 'author,price,cost'
    def __init__(self,author,price,cost): store_attr()
    __repr__ = basic_repr(store_attrs)

ProductPage("Jeremy", 1.50, 0.50)
```




    ProductPage(author=Jeremy, price=1.5, cost=0.5)



One of the most interesting `fastcore` functions is the `funcs_kwargs` decorator. This allows class behavior to be modified without sub-classing. This can allow folks that aren't familiar with object-oriented progressing to customize your class more easily. Here's an example of a class that uses `funcs_kwargs`:

```python
@funcs_kwargs
class T:
    _methods=['some_method']
    def __init__(self, **kwargs): assert not kwargs, f'Passed unknown args: {kwargs}'

p = T(some_method = print)
p.some_method("hello")
```

    hello


The `assert not kwargs` above is used to ensure that the user doesn't pass an unknown parameter (i.e one that's not in `_methods`). `fastai` uses `funcs_kwargs` in many places, for instance, you can customize any part of a `DataLoader` by passing your own methods.

`fastcore` also provides many utility functions that make a Python programmer's life easier, in `fastcore.utils`. We won't look at many here, since you can easily look at the docs yourself. To get you started, have a look at the docs for `chunked` (remember, if you're in a notebook, type `doc(chunked)`), which is a handy function for creating lazily generated batches from a collection.

Python's `ProcessPoolExecutor` is extended to allow `max_workers` to be set to `0`, to easily turn off parallel processing. This makes it easy to debug your code in serial, then run it in parallel. It also allows you to pass arguments to your parallel function, and to ensure there's a pause between calls, in case the process you are running has race conditions. `parallel` makes parallel processing even easier to use, and even adds an optional progress bar.

### L

Like most languages, Python allows for very concise syntax for some very common types, such as `list`, which can be constructed with `[1,2,3]`. Perl's designer Larry Wall explained the reasoning for this kind of syntax:
> In metaphorical honor of Huffman’s compression code that assigns smaller numbers of bits to more common bytes. In terms of syntax, it simply means that commonly used things should be shorter, but you shouldn’t waste short sequences on less common constructs.

On this basis, `fastcore` has just one type that has a single letter name:`L`. The reason for this is that it is designed to be a replacement for `list`, so we want it to be just as easy to use as `[1,2,3]`. Here's how to create that as an `L`:

```python
L(1,2,3)
```




    (#3) [1,2,3]



The first thing to notice is that an `L` object includes in its representation its number of elements; that's the `(#3)` in the output above. If there's more than 10 elements, it will automatically truncate the list:

```python
p = L.range(20).shuffle()
p
```




    (#20) [10,7,9,17,18,4,16,15,19,14...]



`L` contains many of the same indexing ideas that NumPy's `array` does, including indexing with a list of indexes, or a boolean mask list:

```python
p[2,4,6]
```




    (#3) [9,18,16]



It also contains other methods used in `array`, such as `L.argwhere`:

```python
p.argwhere(ge(15))
```




    (#5) [3,4,6,7,8]



As you can see from this example, `fastcore` also includes a number of features that make a functional style of programming easier, such as a full range of boolean functions (e.g `ge`, `gt`, etc) which give the same answer as the functions from Python's `operator` module if given two parameters, but return a [curried function](https://en.wikipedia.org/wiki/Currying) if given one parameter.

There's too much functionality to show it all here, so be sure to check the docs. Many little things are added that we thought should have been in `list` in the first place, such as making this do what you'd expect (which is an error with `list`, but works fine with `L`):

```python
1 + L(2,3,4)
```




    (#4) [1,2,3,4]



### Function dispatch and Transforms

Most Python programmers use object oriented methods and inheritance to allow different objects to behave in different ways even when called with the same method name. Some languages use a very different approach, such as Julia, which uses [multiple dispatch generic functions](https://docs.julialang.org/en/v1/manual/methods/). Python provides [single dispatch generic functions](https://www.python.org/dev/peps/pep-0443/) as part of the standard library. `fastcore` provides multiple dispatch, with the `typedispatch` decorator (which is actually an instance of `DispatchReg`):

```python
@typedispatch
def f_td_test(x:numbers.Integral, y): return x+1
@typedispatch
def f_td_test(x:int, y:float): return x+y

f_td_test(3,2.0), f_td_test(3,2)
```




    (5.0, 4)



This approach to dispatch is particularly useful for adding implementations of functionality in extension modules or user code. It is heavily used in the `Transform` class. A `Transform` is the main building block of the fastai data pipelines. In the most general terms a transform can be any function you want to apply to your data, however the `Transform` class provides several mechanisms that make the process of building them easy and flexible (see the docs for information about each of these):

- Type dispatch
- Dispatch over tuples
- Reversability
- Type propagation
- Preprocessing
- Filtering based on the dataset type
- Ordering
- Appending new behavior with decorators

`Transform` looks for three special methods, <code>encodes</code>, <code>decodes</code>, and <code>setups</code>, which provide the implementation for [`__call__`](https://www.python-course.eu/python3_magic_methods.php), `decode`, and `setup` respectively. For instance:

```python
class A(Transform):
    def encodes(self, x): return x+1

A()(1)
```




    2



For simple transforms like this, you can also use `Transform` as a decorator:

```python
@Transform
def f(x): return x+1

f(1)
```




    2



Transforms can be composed into a `Pipeline`:

```python
@Transform
def g(x): return x/2

pipe = Pipeline([f,g])
pipe(3)
```




    2.0



The power of `Transform` and `Pipeline` is best understood by seeing how they're used to create a complete data processing pipeline. This is explained in [chapter 11](https://github.com/fastai/fastbook/blob/master/11_midlevel_data.ipynb) of the [fastai book](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527), which is [available for free](https://github.com/fastai/fastbook) in Jupyter Notebook format.

## Contributing

After you clone this repository, please run `nbdev_install_git_hooks` in your terminal. This sets up git hooks, which clean up the notebooks to remove the extraneous stuff stored in the notebooks (e.g. which cells you ran) which causes unnecessary merge conflicts.

To run the tests in parallel, launch `nbdev_test_nbs` or `make test`.

Before submitting a PR, check that the local library and notebooks match. The script `nbdev_diff_nbs` can let you know if there is a difference between the local library and the notebooks.
* If you made a change to the notebooks in one of the exported cells, you can export it to the library with `nbdev_build_lib` or `make fastcore`.
* If you made a change to the library, you can export it back to the notebooks with `nbdev_update_lib`.

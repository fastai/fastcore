# Welcome to fastcore
> The Python goodies used in every fast.ai project


## Installing

To install fastcore run: `conda install fastcore` (if you use Anaconda, which we strongly recommend) or `pip install fastcore`. For an [editable install](https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install), clone this repo and run: `pip install -e ".[dev]"`.

## A tour

fastcore contains many features. See the [docs](https://fastcore.fast.ai) for all the details; here's a (somewhat) quick tour of a few higlights.

### Documentation

All fast.ai projects, including this one, are built with [nbdev](https://nbdev.fast.ai), which is a full literate programming environment built on Jupyter Notebooks. That means that every piece of documentation, including the page you're reading now, can be accessed as interactive Jupyter notebooks. In fact, you can even grab a link directly to a notebook running interactively on Google Colab - if you want to follow along with this tour, click the link below, or click the badge at the top of the page:

```python
colab_link('index')
```


[Open `index` in Colab](https://colab.research.google.com/github/fastai/fastcore/blob/master/nbs/index.ipynb)


The full docs are available at [fastcore.fast.ai](https://fastcore.fast.ai). As you'll see, the examples for each function and method are shown as tests, rather than example outputs, so let's start by explaining that.

### Testing

fastcore's testing module is designed to work well with [nbdev](https://nbdev.fast.ai), which is a full literate programming environment built on Jupyter Notebooks. fastcore and nbdev's approach to testing starts with the premise that all your tests should pass. If one fails, no more tests in a notebook are run.

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

So every test shown in the docs is also showing you the behavior of the library --- and visa versa!

Test functions always start with `test_`, and then follow with the operation being tested. So `test_eq` tests for equality (as you saw in the example above). This includes tests for equality of arrays and tensors, lists and generators, and many more:

```python
test_eq([0,1,2,3], np.arange(4))
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

## Foundations

fast.ai is unusual in that we often use [mixins](https://en.wikipedia.org/wiki/Mixin) in our code. Mixins are widely used in many programming languages, such as Ruby, but not so much in Python. We use mixins to attach new behavior to existing libraries, or to allow modules to add new behavior to our own classes, such as in extension modules. One useful example of a mixin we define is `Path.ls`, which lists a directory and returns an `L` (an extended list class which we'll discuss shortly):

```python
p = Path('images')
p.ls()
```




    (#2) [Path('images/puppy.jpg'),Path('images/mnist3.png')]



You can easily add you own mixins with the `patch` [decorator](https://realpython.com/primer-on-python-decorators/), which takes advantage of Python 3 [function annotations](https://www.python.org/dev/peps/pep-3107/#parameters) to say what class to patch:

```python
@patch
def say_hello(x:Path): print('Why hello there')

p.say_hello()
```

    Why hello there


We also use `**kwargs` frequently. In python `**kwargs` in a parameter like means “put any additional keyword arguments into a dict called `kwargs`. Normally, using `kwargs` makes an API quite difficult to work with, because because it breaks things like tab-completion and popup lists of signatures. `fastcore.utils` provides `use_kwargs` and `delegates` to avoid this problem. See our [detailed article on delegation](https://www.fast.ai/2019/08/06/delegation/) on this topic.

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
    def __init__(self,author,price,cost): store_attr(self)
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


The `assert not kwargs` there is used to ensure that the user doesn't pass an unknown parameter (i.e one that's not in `_methods`). `fastai` uses `funcs_kwargs` in many places, for instance, you can customize any part of a `DataLoader` by passing your own methods.

TODO

- `L`

## Contributing

After you clone this repository, please run `nbdev_install_git_hooks` in your terminal. This sets up git hooks, which clean up the notebooks to remove the extraneous stuff stored in the notebooks (e.g. which cells you ran) which causes unnecessary merge conflicts.

To run the tests in parallel, launch `nbdev_test_nbs` or `make test`.

Before submitting a PR, check that the local library and notebooks match. The script `nbdev_diff_nbs` can let you know if there is a difference between the local library and the notebooks.
* If you made a change to the notebooks in one of the exported cells, you can export it to the library with `nbdev_build_lib` or `make fastcore`.
* If you made a change to the library, you can export it back to the notebooks with `nbdev_update_lib`.

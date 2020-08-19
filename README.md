# Welcome to fastcore
> The Python goodies used in every fast.ai project


## Installing

To install fastcore run: `conda install fastcore` (if you use Anaconda, which we strongly recommend) or `pip install fastcore`. For an [editable install](https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install), clone this repo and run: `pip install -e ".[dev]"`.

## A tour

fastcore contains many features. See the [docs](https://fastcore.fast.ai) for all the details; here's a (somewhat) quick tour of a few higlights.

### Documentation

All fast.ai projects, including this one, are built with [nbdev](https://nbdev.fast.ai), which is a full literate programming environment built on Jupyter Notebooks. That means that every piece of documentation, including the page you're reading now, can be accessed as interactive Jupyter notebooks. In fact, you can even grab a link directly to a notebook running interactively on Google Colab - if you want to follow along with this tour, click the link below:

```python
colab_link('index')
```


[Open `index` in Colab](https://colab.research.google.com/github/fastai/fastcore/blob/master/nbs/index.ipynb)


(tour currently under construction)

### Testing

fastcore's testing module is designed to work well with [nbdev](https://nbdev.fast.ai), which is a full literate programming environment built on Jupyter Notebooks. fastcore and nbdev's approach to testing starts with the premise that all your tests should pass. If one fails, no more tests in a notebook are run.

## Contributing

After you clone this repository, please run `nbdev_install_git_hooks` in your terminal. This sets up git hooks, which clean up the notebooks to remove the extraneous stuff stored in the notebooks (e.g. which cells you ran) which causes unnecessary merge conflicts.

To run the tests in parallel, launch `nbdev_test_nbs` or `make test`.

Before submitting a PR, check that the local library and notebooks match. The script `nbdev_diff_nbs` can let you know if there is a difference between the local library and the notebooks.
* If you made a change to the notebooks in one of the exported cells, you can export it to the library with `nbdev_build_lib` or `make fastcore`.
* If you made a change to the library, you can export it back to the notebooks with `nbdev_update_lib`.

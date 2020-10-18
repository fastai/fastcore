# Release notes

<!-- do not remove -->

## 1.2.2

### New Features

- support `store_true` and `store_false` in `fastcore.script` ([#137](https://github.com/fastai/fastcore/issues/137))
- add function `otherwise` ([#136](https://github.com/fastai/fastcore/issues/136))
- add `pdb` debug flag to scripts ([#133](https://github.com/fastai/fastcore/issues/133))

### Bugs Squashed

- Fix `copy_func` to include required keyword defaults ([#134](https://github.com/fastai/fastcore/pull/134)), thanks to [@worc3131](https://github.com/worc3131)


## 1.2.0

### Breaking Changes

- `Config` no longer magically converts `str->Path` for some keys. Use new `path` method instead ([#131](https://github.com/fastai/fastcore/issues/131))

### New Features

- `rinstance`: Curried `isinstance` but with args reversed, suitable for `partial` ([#130](https://github.com/fastai/fastcore/issues/130))
- Use `_repr_pretty_` for `L` ([#129](https://github.com/fastai/fastcore/issues/129))
- `open_file` to open optionally-compressed files for reading and writing, and add compression support to `load_pickle` and `save_pickle` ([#128](https://github.com/fastai/fastcore/issues/128))
- add context manager for failed tests ([#126](https://github.com/fastai/fastcore/pull/126)), thanks to [@hamelsmu](https://github.com/hamelsmu)

### Bugs Squashed

- `urlread` does not work with `Request.request` ([#132](https://github.com/fastai/fastcore/issues/132))


## 1.1.2

### New Features

- runtime type checking with `typed` decorator ([#125](https://github.com/fastai/fastcore/issues/125))


## 1.1.1

### New Features

- `threaded` decorator ([#124](https://github.com/fastai/fastcore/issues/124))
- POST support for `urlread` ([#124](https://github.com/fastai/fastcore/issues/124))
- add `sorted_ex, `map_ex`, `filter_ex`, and `argwhere` ([#122](https://github.com/fastai/fastcore/issues/122))


## 1.1.0

### Breaking Changes

- Remove `Path.{read,write}` (use `Path.{read_text,write_text}` instead) and change `Path.{load,save}` to functions `load_pickle` and `save_pickle` ([#121](https://github.com/fastai/fastcore/issues/121))

## 1.0.22

### New Features

- add `L.setattrs`, inspired by Saul Pwanson ([#117](https://github.com/fastai/fastcore/issues/117))
- move `Config` from `nbdev` ([#116](https://github.com/fastai/fastcore/issues/116))
- add `nested_attr` and use it in `L.attrgot` ([#115](https://github.com/fastai/fastcore/issues/115))


## 1.0.21

### Deprecations (will be removed in future release)

- `patch_property`: use `patch(as_prop=True)` instead

### New Features

- New param `cast` for `store_attr` and new decorator `with_cast` ([#114](https://github.com/fastai/fastcore/issues/114))
- add `L.insert` and `exec_local` ([#113](https://github.com/fastai/fastcore/issues/113))
- Patch decorator with optional argument ([#110](https://github.com/fastai/fastcore/pull/110)), thanks to [@Salehbigdeli](https://github.com/Salehbigdeli)
- Make typedispatch decorator more general ([#106](https://github.com/fastai/fastcore/pull/106)), thanks to [@Salehbigdeli](https://github.com/Salehbigdeli)

### Bugs Squashed

- Fix default in oper ([#112](https://github.com/fastai/fastcore/pull/112)), thanks to [@Salehbigdeli](https://github.com/Salehbigdeli)
- Inconsistency with `cmp_instance` and `typedispatch` because of binary sort algorithm ([#100](https://github.com/fastai/fastcore/issues/100))


## 1.0.20

### New Features

- add `ignore_ex=False` and `as_bytes=False` params to `run` ([#108](https://github.com/fastai/fastcore/issues/108))
- `AttrDict`: a `dict` subclass that also provides access to keys as attrs; and change `dict2obj` to create `AttrDict`s instead of `SimpleNamespace`s ([#107](https://github.com/fastai/fastcore/issues/107))


## 1.0.19

### New Features

- `run`: flexibly run an external process and raise exception if it fails ([#105](https://github.com/fastai/fastcore/issues/105))


## 1.0.16

### New Features

- add `threadpool=False` param to `parallel` to use threads instead of processes ([#102](https://github.com/fastai/fastcore/issues/102))


## 1.0.15

### New Features

- add `L.map_filter` and `L.map_first` ([#97](https://github.com/fastai/fastcore/issues/97))
  - These support some nice refactorings, like changing from this:
    ```python
    d = []
    for c in cs:
      m = f(c)
      if not m:
        continue
      d.append(m.group(1))
    ```
    to this:
    ```python
    d = cs.map_filter(f).map(Self.group(1))
    ```


## 1.0.14

### Bugs Squashed

- Reapply fix for #86 which was unintentionally reverted by the next commit ([#91](https://github.com/fastai/fastcore/issues/91))

## 1.0.13

### New Features

- `dict2obj`: Convert (possibly nested) dicts (or lists of dicts) to `SimpleNamespace` ([#90](https://github.com/fastai/fastcore/issues/90))

## 1.0.12

### New Features

- add function support to `store_attr` ([#85](https://github.com/fastai/fastcore/issues/85))

### Bugs Squashed

- `mp_context` keyword for initialising concurrent.futures.ProcessPoolExecutor only supported in python 3.7+ ([#86](https://github.com/fastai/fastcore/issues/86))

## 1.0.10

### Breaking Changes

- remove `parallel_chunked`, use `chunksize` arg to `parallel` instead ([#81](https://github.com/fastai/fastcore/issues/81))

### New Features

- move fastscript to fastcore.script ([#84](https://github.com/fastai/fastcore/issues/84))
- add `run_proc` and `do_request` ([#83](https://github.com/fastai/fastcore/issues/83))
- added `chunksize` to `parallel`, which passes to `ProcessPoolExecutor.map` ([#82](https://github.com/fastai/fastcore/issues/82))
- move metaclasses and delegates et al to new `meta` module ([#80](https://github.com/fastai/fastcore/issues/80))

## 1.0.4

### New Features

- Remove numpy prerequisite ([#75](https://github.com/fastai/fastcore/issues/75))
  - NB: fastcore's `L` and other collection features still work with numpy
    arrays, but they do so internally using instance methods, so numpy is no longer a
    prerequisite, and numpy is not loaded if not used

## 1.0.2

### Bugs Squashed

- "has default params. These will be ignored" shown when not appropriate ([#74](https://github.com/fastai/fastcore/issues/74))

## 1.0.1

### Breaking Changes

- Change arguments of `store_attr()` and remove `store_attrs` attribute ([#71](https://github.com/fastai/fastcore/pull/71))
  - `store_attr`'s API has changed. `self` is now the second parameter, and is optional. Previously, if no names were passed to store,
    names were taken from the `store_attrs` attribute; now, however, names are taken from the list of arguments to the current function.

### New Features

- Warn if defaults passed to `typedispatch` ([#73](https://github.com/fastai/fastcore/pull/73))

- Add `urlread` and `urljson` ([#72](https://github.com/fastai/fastcore/pull/72))

## Version 1.0.0

- Initial release


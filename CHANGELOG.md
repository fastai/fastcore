# Release notes

<!-- do not remove -->

## 1.3.26

### New Features

- add class init support to docments ([#347](https://github.com/fastai/fastcore/issues/347))
- add timeout param to url functions ([#346](https://github.com/fastai/fastcore/issues/346))
- add `L.argfirst` ([#345](https://github.com/fastai/fastcore/issues/345))
- add `Path.relpath` ([#344](https://github.com/fastai/fastcore/issues/344))
- add `full` and `returns` to `docments`, and derive type from default in `fastcore.script` ([#342](https://github.com/fastai/fastcore/issues/342))
- allow use of `docments` in `fastcore.script.call_parse` ([#341](https://github.com/fastai/fastcore/issues/341))
- add `docments` ([#340](https://github.com/fastai/fastcore/issues/340))


## 1.3.25

### Bugs Squashed

- `untar_dir` always extracts archive even if already exists ([#337](https://github.com/fastai/fastcore/issues/337))


## 1.3.23

### New Features

- Support py36 in `untar_dir`

## 1.3.22

### New Features

- New method: `Path.delete()` to remove a file or directory ([#336](https://github.com/fastai/fastcore/issues/336))
- Add `urlretrieve`, which as same as `urllib.request.urlretrieve` but also works with `Request` objects ([#335](https://github.com/fastai/fastcore/issues/335))


## 1.3.21

### New Features

- remove fastai-specific pieces from `Config` ([#334](https://github.com/fastai/fastcore/issues/334))
- in `untar_dir` create a directory if there is more than one item in root of archive ([#333](https://github.com/fastai/fastcore/issues/333))
- allow directory `dest` in `urlsave` ([#327](https://github.com/fastai/fastcore/issues/327))


## 1.3.20

### New Features

- make patch more compatible with classmethods ([#309](https://github.com/fastai/fastcore/pull/309)), thanks to [@tezike](https://github.com/tezike)
- Added order and list support for Pipeline.add ([#297](https://github.com/fastai/fastcore/pull/297)), thanks to [@marii-moe](https://github.com/marii-moe)
- support windows: only add lock if it runs parallelly ([#283](https://github.com/fastai/fastcore/pull/283)), thanks to [@mszhanyi](https://github.com/mszhanyi)

### Bugs Squashed

- fix #304 UnicodeDecodeError while downloading git archive ([#308](https://github.com/fastai/fastcore/pull/308)), thanks to [@pradeepbbl](https://github.com/pradeepbbl)
- Fix saving str as bytes in urlsave ([#278](https://github.com/fastai/fastcore/pull/278)), thanks to [@jochym](https://github.com/jochym)


## 1.3.19


### Bugs Squashed

- `sparkline` errors when a value is given that exceeds `mx` ([#277](https://github.com/fastai/fastcore/issues/277))


## 1.3.17

### New Features

- add `strcat` and `mapt` ([#273](https://github.com/fastai/fastcore/issues/273))


## 1.3.14

### New Features

- add `loads_multi` ([#271](https://github.com/fastai/fastcore/issues/271))

### Bugs Squashed

- ignored empty str `names` in `store_attr` ([#267](https://github.com/fastai/fastcore/issues/267))
- `returns_none` not returning non-none type ([#266](https://github.com/fastai/fastcore/issues/266))
- `Transform` return type ignored ([#265](https://github.com/fastai/fastcore/issues/265))
- `test_eq` incorrect for pandas `DataFrame` ([#188](https://github.com/fastai/fastcore/pull/188)), thanks to [@kessido](https://github.com/kessido)


## 1.3.13

### New Features
- add  `EventTimer` ([#263](https://github.com/fastai/fastcore/issues/263))
- Store kwargs in `store_attr  ([#262](https://github.com/fastai/fastcore/issues/262))
- add `truncstr` ([#261](https://github.com/fastai/fastcore/issues/261))
- add `sparkline` ([#260](https://github.com/fastai/fastcore/issues/260))
- add `autostart` for generators ([#249](https://github.com/fastai/fastcore/issues/249))
- dynamic fastcore.script help width ([#247](https://github.com/fastai/fastcore/issues/247))
- optional override to `risinstance` to support both types and str in the same function ([#191](https://github.com/fastai/fastcore/pull/191)), thanks to [@kessido](https://github.com/kessido)

### Bugs Squashed

- delegates doesn't pull the `__init__` of a class ([#217](https://github.com/fastai/fastcore/issues/217))
- `test_eq` incorrect for pandas `DataFrame` ([#188](https://github.com/fastai/fastcore/pull/188)), thanks to [@kessido](https://github.com/kessido)


## 1.3.12

### New Features

- enum support for `call_parse` ([#245](https://github.com/fastai/fastcore/issues/245))
- Added obj2dict ([#244](https://github.com/fastai/fastcore/issues/244))
- `return_headers` param for `urlsend` and `urlread` ([#242](https://github.com/fastai/fastcore/issues/242))
- add common Chrome headers ([#241](https://github.com/fastai/fastcore/issues/241))
- add `utc2local` and `local2utc` ([#239](https://github.com/fastai/fastcore/issues/239))
- add `Path.read_json` ([#238](https://github.com/fastai/fastcore/issues/238))

### Bugs Squashed

- `*args` not handled correctly in process/thread pools ([#246](https://github.com/fastai/fastcore/issues/246))


## 1.3.11

### Bugs Squashed

- regression in urlopen header user-agent not set ([#237](https://github.com/fastai/fastcore/issues/237))
- `loads` incompatible with Python 3.9 ([#236](https://github.com/fastai/fastcore/issues/236))
- Documentation search not working ([#235](https://github.com/fastai/fastcore/issues/235))


## 1.3.10

### New Features

- split `parallel` and `net` modules out of `xtras` ([#234](https://github.com/fastai/fastcore/issues/234))
- New HTTP Exceptions hierarchy for each status code, used by `url*` functions
- add `Request.summary` and `debug` paramaeter to `urlsend` ([#233](https://github.com/fastai/fastcore/issues/233))
- Add `ImportEnum`, `StrEnum`, and `str_enum` ([#232](https://github.com/fastai/fastcore/issues/232))
- handle encoded data in `urlrequest` ([#231](https://github.com/fastai/fastcore/issues/231))


## 1.3.9

### New Features

- use `__slots__` in `store_attr` if exists ([#226](https://github.com/fastai/fastcore/issues/226))
- add `urlrequest` ([#225](https://github.com/fastai/fastcore/issues/225))
- add `loads` and `urlsend` ([#224](https://github.com/fastai/fastcore/issues/224))
- add `PartialFormatter` and `partial_format` ([#223](https://github.com/fastai/fastcore/issues/223))
- add `stringfmt_names` ([#222](https://github.com/fastai/fastcore/issues/222))


## 1.3.8

### New Features

- rename `negate_func` to `not_` for consistency with other curried ops ([#221](https://github.com/fastai/fastcore/issues/221))
- Support empty content for `urljson` ([#219](https://github.com/fastai/fastcore/issues/219))
- move `patch` and `patch_to` to `fastcore.basics`, and avoid clobbering existing symbols when patching ([#214](https://github.com/fastai/fastcore/issues/214))


## 1.3.7

### New Features

- add `startthread` ([#218](https://github.com/fastai/fastcore/issues/218))
- make `run` compatible with py36 ([#216](https://github.com/fastai/fastcore/issues/216))
- `reuse_addr` param to `start_server` ([#215](https://github.com/fastai/fastcore/issues/215))
- add rfc3986 list to `urlquote` ([#213](https://github.com/fastai/fastcore/issues/213))


## 1.3.6

### New Features

- quote URL paths in `urlwrap` ([#211](https://github.com/fastai/fastcore/issues/211))
- Add `start_server` and `start_client` for simple socket networking ([#210](https://github.com/fastai/fastcore/issues/210))
- new `uniqueify` and `val2idx` functions, and additional params to `listify` ([#209](https://github.com/fastai/fastcore/issues/209))
- improve representation in `basic_repr` ([#197](https://github.com/fastai/fastcore/issues/197))


## 1.3.5

### Breaking Changes

- remove `log_args` ([#176](https://github.com/fastai/fastcore/issues/176))

### New Features

- `Stateful` base class/mixin for objects that should not serialize all their state ([#196](https://github.com/fastai/fastcore/issues/196))
- new `frame` param to `argnames` ([#195](https://github.com/fastai/fastcore/issues/195))
- add `urlopen` and `untar_dir` ([#192](https://github.com/fastai/fastcore/issues/192))
- `SCRIPT_INFO.func` to let functions know what CLI name was called in `fastcore.script` ([#185](https://github.com/fastai/fastcore/issues/185))
- add `annotations` and `argnames` functions ([#179](https://github.com/fastai/fastcore/issues/179))
- allow `but` param in `store_attr` to be either `list` or `str` ([#174](https://github.com/fastai/fastcore/issues/174))
- add `urlvalid` ([#173](https://github.com/fastai/fastcore/issues/173))

### Bugs Squashed

- `@typed` doesn't work with classes ([#183](https://github.com/fastai/fastcore/issues/183)) (reported by @krishnap)


## 1.3.2

### New Features

- add `repr_dict` and use for display for `AttrDict` ([#172](https://github.com/fastai/fastcore/issues/172))
- add `urlsave`, `urlclean`, and `repo_details` ([#171](https://github.com/fastai/fastcore/issues/171))
- `remove_suffix` function ([#170](https://github.com/fastai/fastcore/issues/170))
- add `urlcheck` and `urlwrap` ([#168](https://github.com/fastai/fastcore/issues/168))
- new `AutoInit` mixin ([#165](https://github.com/fastai/fastcore/issues/165))

### Bugs Squashed

- `risinstance` fails if param is not truthy ([#166](https://github.com/fastai/fastcore/issues/166))


## 1.3.1

### New Features

- callable support for `Self` ([#162](https://github.com/fastai/fastcore/issues/162))
- add filter func to `first` ([#161](https://github.com/fastai/fastcore/issues/161))
- `maybe_open` context manager and fast `image_size` funcion ([#160](https://github.com/fastai/fastcore/issues/160))

### Bugs Squashed

- Redundent `L.map_filter` removed (since `L.map.filter` does the same thing)


## 1.3.0

### Breaking Changes

- `change param name `copy_meta`->`as_copy` in `retain_meta` ([#157](https://github.com/fastai/fastcore/issues/157))

### New Features

- `groupby` extensions for `int` and `str` instead of callables, and an optional `val` transform ([#155](https://github.com/fastai/fastcore/issues/155))
- add `modified_env` ([#148](https://github.com/fastai/fastcore/issues/148))

### Bugs Squashed

- `coll_repr` printing incorrectly when `max_n`!=10 ([#154](https://github.com/fastai/fastcore/pull/154)), thanks to [@kessido](https://github.com/kessido)


## 1.2.5

### New Features

- add `true`, `NullType`, `null`, and `tonull` ([#153](https://github.com/fastai/fastcore/issues/153))
- add `working_directory` ([#151](https://github.com/fastai/fastcore/issues/151))
- move `bind` et al to `fastcore.basics` ([#150](https://github.com/fastai/fastcore/issues/150))


## 1.2.4

### New Features

- move basic functionality into `fastcore.basics`, using minimal imports ([#149](https://github.com/fastai/fastcore/issues/149))
- add `anno_dict` and `empty2none` in `meta` ([#145](https://github.com/fastai/fastcore/issues/145))


## 1.2.3

### New Features

- add `try_attrs` ([#142](https://github.com/fastai/fastcore/issues/142))
- add `filter_dict`, `filter_keys`, and `filter_values` ([#140](https://github.com/fastai/fastcore/issues/140))
- add `str2bool` ([#138](https://github.com/fastai/fastcore/issues/138))

### Bugs Squashed

- `type` fails with `@typedispatch` ([#144](https://github.com/fastai/fastcore/issues/144))
- `with_cast` fails to cast default values ([#139](https://github.com/fastai/fastcore/issues/139))


## 1.2.2

### New Features

- support `store_true` and `store_false` in `fastcore.script` ([#137](https://github.com/fastai/fastcore/issues/137))
- add function `otherwise` ([#136](https://github.com/fastai/fastcore/issues/136))
- add `pdb` debug flag to scripts ([#133](https://github.com/fastai/fastcore/issues/133))
- Update `copy_func` to include required keyword defaults ([#134](https://github.com/fastai/fastcore/pull/134)), thanks to [@worc3131](https://github.com/worc3131)


## 1.2.0

### Breaking Changes

- `Config` no longer magically converts `str->Path` for any keys. Use new `path` method instead ([#131](https://github.com/fastai/fastcore/issues/131))

### New Features

- `rinstance`: Curried `isinstance` but with args reversed, suitable for `partial` ([#130](https://github.com/fastai/fastcore/issues/130))
- Use `_repr_pretty_` for `L` ([#129](https://github.com/fastai/fastcore/issues/129))
- `open_file` to open optionally-compressed files for reading and writing, and add compression support to `load_pickle` and `save_pickle` ([#128](https://github.com/fastai/fastcore/issues/128))
- add context manager for failed tests ([#126](https://github.com/fastai/fastcore/pull/126)), thanks to [@hamelsmu](https://github.com/hamelsmu)
- Add `Request.request` support to `urlread` ([#132](https://github.com/fastai/fastcore/issues/132))


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


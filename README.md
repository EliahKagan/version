<!-- SPDX-License-Identifier: 0BSD -->

# version - Version metadata retrieval and type checking

This compares a few ways to give a Python project version metadata and a
top-level `__version__` attribute, while specifying the version in only one
place, and where `mypy` and `pyright` can still do strict type checking.

This is not exhaustive. There are other techniques besides the ones shown here.
In addition, this only shows how to apply the techniques when configuring the
package in `pyproject.toml` and using `setuptools` as a build backend.

## License

[0BSD](https://spdx.org/licenses/0BSD). See[**`LICENSE`**](LICENSE).

## Approaches shown

- [**`by_literal/`**](by_literal/) - Set the value of `__version__` in the
  package's top-level `__init__.py`, and have the build backend [parse it
  out](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#dynamic-metadata).

- [**`by_getattr/`**](by_getattr/) - Define `__getattr__` in the package's
  top-level `__init__.py` that [dynamically retrieves version
  metadata](https://docs.python.org/3/library/importlib.metadata.html#distribution-versions)
  on demand when `__version__` is accessed. (This requires some extra work to
  get precise type hinting, since `mypy` rejects `Literal["__version__"]` as a
  parameter type annotation for module-level `__getattr__`.)

- [**`by_property/`**](by_property/) - Create a subclass of `ModuleType` with a
  `__version__` *property* that [dynamically retrieves version
  metadata](https://docs.python.org/3/library/importlib.metadata.html#distribution-versions)
  on demand. Rebind the package's `__class__` attribute to that new class.

## Running checks

Checks can be run together with [`tox`](https://tox.wiki/).

To do so, install `tox` if it is not already installed. Make sure you have
version 4 or higher.

Then, at the top of this repository's working tree (the direcctory that
contains `tox.ini`), test and typecheck any of the individual packages as
follows:

```sh
tox --root by_literal
```

```sh
tox --root by_getattr
```

```sh
tox --root by_property
```

## Further reading

- [Single-sourcing the package
  version](https://packaging.python.org/en/latest/guides/single-sourcing-package-version/)
- [3.3.2.1. Customizing module attribute
  access](https://docs.python.org/3/reference/datamodel.html#customizing-module-attribute-access)

"""Package that gets its :attr:`__version__` dynamically with a property."""

import sys
import types
from typing import List


class _ModuleWithVersion(types.ModuleType):
    """Module whose :attr:`__version__` is obtained from dynamic metadata."""

    def __dir__(self) -> List[str]:
        return [*super().__dir__(), "__version__"]

    @property
    def __version__(self) -> str:
        if sys.version_info >= (3, 8):
            from importlib.metadata import version
        else:
            from importlib_metadata import version

        return version(self.__name__)


sys.modules[__name__].__class__ = _ModuleWithVersion

__version__: str


def hello() -> None:
    """Print a simple greeting."""
    print("Hello, world!")

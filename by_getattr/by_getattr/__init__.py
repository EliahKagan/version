"""Package that gets its :attr:`__version__` dynamically with :func:`__getattr__`."""

import sys
from typing import Literal, TYPE_CHECKING

__version__: str


def _getattr(name: Literal["__version__"]) -> str:
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    if sys.version_info >= (3, 8):
        from importlib.metadata import version
    else:
        from importlib_metadata import version

    return version(__name__)


if not TYPE_CHECKING:
    __getattr__ = _getattr


def hello() -> None:
    """Print a simple greeting."""
    print("Hello, world!")
"""Tests for the :mod:`by_property` package."""

import subprocess
import sys

import pytest

import by_property

if sys.version_info >= (3, 8):
    from importlib.metadata import version as _version
else:
    from importlib_metadata import version as _version

_EXPECTED_VERSION = "0.1.0"


def test_hello_function(capsys: pytest.CaptureFixture) -> None:
    by_property.hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"


def test_hello_command() -> None:
    process = subprocess.run(
        "hello",  # noqa: S607  # OK in tests, would be insecure in general.
        capture_output=True,
        check=True,
        text=True,
    )
    assert process.stdout == "Hello, world!\n"


def test_version_attribute() -> None:
    actual_version = by_property.__version__
    assert actual_version == _EXPECTED_VERSION


def test_version_metadata() -> None:
    actual_version = _version(by_property.__name__)
    assert actual_version == _EXPECTED_VERSION


def test_nonexistent_attribute() -> None:
    with pytest.raises(
        AttributeError,
        match=r"\Amodule 'by_property' has no attribute 'nonexistent'\Z",
    ):
        by_property.nonexistent  # type: ignore[attr-defined]


def test_dir_lists_common_dunders() -> None:
    common = {'__doc__', '__loader__', '__name__', '__package__', '__spec__'}
    assert common <= set(dir(by_property))


def test_dir_lists_hello_attribute() -> None:
    assert "hello" in dir(by_property)


def test_dir_lists_version_attribute() -> None:
    assert "__version__" in dir(by_property)

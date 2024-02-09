"""Tests for the :mod:`by_literal` package."""

import subprocess
import sys

import pytest

import by_literal

if sys.version_info >= (3, 8):
    from importlib.metadata import version as _version
else:
    from importlib_metadata import version as _version

_EXPECTED_VERSION = "0.1.0"


def test_hello_function(capsys: pytest.CaptureFixture) -> None:
    by_literal.hello()
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
    actual_version = by_literal.__version__
    assert actual_version == _EXPECTED_VERSION


def test_version_metadata() -> None:
    actual_version = _version(by_literal.__name__)
    assert actual_version == _EXPECTED_VERSION

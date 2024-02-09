"""Tests for the :mod:`by_literal` package."""

import importlib.metadata

import pytest

import by_literal

_EXPECTED_VERSION = "0.1.0"


def test_hello(capsys: pytest.CaptureFixture) -> None:
    by_literal.hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"


def test_version_attribute() -> None:
    actual_version = by_literal.__version__
    assert actual_version == _EXPECTED_VERSION


def test_version_metadata() -> None:
    actual_version = importlib.metadata.version(by_literal.__name__)
    assert actual_version == _EXPECTED_VERSION

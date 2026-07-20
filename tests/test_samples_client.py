import httpx
import pytest
import respx
from conftest import SAMPLE_C

from mini_nucleiq.samples import HttpSamplesClient

BASE = "https://raw.githubusercontent.com/cellsia/mini-nucleiq-code-challenge/main/samples"


@respx.mock
def test_get_sample_should_return_sample() -> None:
    respx.get(f"{BASE}/sample-c.json").mock(
        return_value=httpx.Response(
            200, json={"name": "sample-c", "cells": SAMPLE_C}
        )
    )

    result = HttpSamplesClient().get_sample("sample-c")

    assert result == SAMPLE_C

@respx.mock
def test_get_sample_should_raise_if_missing_sample() -> None:
    respx.get(f"{BASE}/missing.json").mock(return_value=httpx.Response(404))

    with pytest.raises(httpx.HTTPStatusError):
        HttpSamplesClient().get_sample("missing")

@respx.mock
def test_get_sample_should_raise_if_error() -> None:
    respx.get(f"{BASE}/sample-c.json").mock(return_value=httpx.Response(500))

    with pytest.raises(httpx.HTTPStatusError):
        HttpSamplesClient().get_sample("sample-c")
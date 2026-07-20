import httpx
import respx
from conftest import SAMPLE_C

from mini_nucleiq.analysis import AnalysisDecision, analyze_sample
from mini_nucleiq.samples import HttpSamplesClient

BASE = "https://raw.githubusercontent.com/cellsia/mini-nucleiq-code-challenge/main/samples"

@respx.mock
def test_full_analysis_with_real_client() -> None:
    respx.get(f"{BASE}/sample-c.json").mock(
        return_value=httpx.Response(200, json={"name": "sample-c", "cells": SAMPLE_C})
    )

    result = analyze_sample(
        "sample-c",
        algorithms=["even-zeroes", "contiguous-ones", "surrounded-ones"],
        samples_client=HttpSamplesClient(),
    )

    assert result.decision is AnalysisDecision.NEGATIVE
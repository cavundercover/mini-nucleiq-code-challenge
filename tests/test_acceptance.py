from doubles import StubSamplesClient

from mini_nucleiq.analysis import (
    AnalysisDecision,
    AnalysisResult,
    analyze_sample,
)
from mini_nucleiq.samples import Sample


def test_should_analyze_sample_c_negative(sample_c: Sample) -> None:
    samples_client = StubSamplesClient(sample_c)

    result = analyze_sample(
        "sample-c",
        algorithms=["even-zeroes", "contiguous-ones", "surrounded-ones"],
        samples_client=samples_client,
    )

    assert result == AnalysisResult(decision=AnalysisDecision.NEGATIVE)

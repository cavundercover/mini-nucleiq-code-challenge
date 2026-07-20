import pytest

from doubles import StubSamplesClient

from mini_nucleiq.analysis import AnalysisDecision, analyze_sample


def test_analyze_sample_should_be_positive_when_more_than_half_algorithms_are_positive() -> (
    None
):
    sample = [0, 1, 0]
    client = StubSamplesClient(sample)

    result = analyze_sample(
        "test", algorithms=["even-zeroes", "surrounded-ones"], samples_client=client
    )

    assert result.decision is AnalysisDecision.POSITIVE


def test_analyze_sample_should_be_negative_when_half_algorithms_are_positive() -> None:
    sample = [0, 1]
    client = StubSamplesClient(sample)

    result = analyze_sample(
        "test", algorithms=["even-zeroes", "surrounded-ones"], samples_client=client
    )

    assert result.decision is AnalysisDecision.NEGATIVE


def test_analyze_sample_should_raise_error_on_unknown_algorithm() -> None:
    sample = [0, 1]
    client = StubSamplesClient(sample)

    with pytest.raises(ValueError, match="Unknown algorithm made-up"):
        analyze_sample(
            "test", algorithms=["made-up", "surrounded-ones"], samples_client=client
        )

def test_analyze_sample_should_raise_error_on_empty_algorithm_list() -> None:
    sample = [0, 1]
    client = StubSamplesClient(sample)

    with pytest.raises(ValueError, match="No algorithms were selected"):
        analyze_sample(
            "test", algorithms=[], samples_client=client
        )

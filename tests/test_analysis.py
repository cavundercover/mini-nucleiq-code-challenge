import pytest
from conftest import SAMPLE_C
from doubles import StubSamplesClient

from mini_nucleiq.algorithms import AlgorithmDecision
from mini_nucleiq.analysis import AnalysisDecision, analyze_sample


def test_analyze_sample_should_be_positive_when_more_half_algorithms_are_positive() -> (
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
        analyze_sample("test", algorithms=[], samples_client=client)


def test_analyze_includes_algorithm_results() -> None:
    sample = SAMPLE_C
    client = StubSamplesClient(sample)

    result = analyze_sample(
        "sample-c",
        algorithms=["even-zeroes", "contiguous-ones", "surrounded-ones"],
        samples_client=client,
    )

    even_zeroes_result = result.algorithm_results["even-zeroes"]
    assert even_zeroes_result.decision is AlgorithmDecision.NEGATIVE
    assert even_zeroes_result.positive_cells_count == 3
    assert even_zeroes_result.positivity == pytest.approx(0.3)
    contiguous_result = result.algorithm_results["contiguous-ones"]
    assert contiguous_result.decision is AlgorithmDecision.NEGATIVE
    assert contiguous_result.positive_cells_count == 2
    assert contiguous_result.positivity == pytest.approx(0.2)
    surrounded_result = result.algorithm_results["surrounded-ones"]
    assert surrounded_result.decision is AlgorithmDecision.POSITIVE
    assert surrounded_result.positive_cells_count == 2
    assert surrounded_result.positivity == pytest.approx(0.2)

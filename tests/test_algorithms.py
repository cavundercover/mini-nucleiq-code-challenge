import pytest
from conftest import SAMPLE_C

from mini_nucleiq.algorithms import (
    AlgorithmDecision,
    even_zeroes,
)
from mini_nucleiq.samples import Sample


@pytest.mark.parametrize(
    ("sample", "expected_count", "expected_positivity", "expected_decision"),
    [
        pytest.param(SAMPLE_C, 3, 0.3, AlgorithmDecision.NEGATIVE, id="sample_c"),
        pytest.param(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            6,
            0.5,
            AlgorithmDecision.POSITIVE,
            id="all_0",
        ),
        pytest.param(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            0,
            0,
            AlgorithmDecision.NEGATIVE,
            id="all_1",
        ),
        pytest.param([0], 1, 1, AlgorithmDecision.POSITIVE, id="only_one_0"),
        pytest.param([1], 0, 0, AlgorithmDecision.NEGATIVE, id="only_one_1"),
    ],
)
def test_even_zeroes(
    sample: Sample,
    expected_count: int,
    expected_positivity: float,
    expected_decision: AlgorithmDecision,
) -> None:
    result = even_zeroes(sample)

    assert result.decision is expected_decision
    assert result.positivity == pytest.approx(expected_positivity)
    assert result.positive_cells_count == expected_count


def test_even_zeroes_should_reject_empty_sample() -> None:
    with pytest.raises(ValueError, match="Sample is empty"):
        even_zeroes([])

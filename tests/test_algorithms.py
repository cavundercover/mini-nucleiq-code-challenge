import pytest
from conftest import SAMPLE_C

from mini_nucleiq.algorithms import (
    ALGORITHMS,
    AlgorithmDecision,
    run_algorithm,
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
        pytest.param(
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
            4,
            4 / 13,
            AlgorithmDecision.POSITIVE,
            id="above_30_percent",
        ),
    ],
)
def test_even_zeroes(
    sample: Sample,
    expected_count: int,
    expected_positivity: float,
    expected_decision: AlgorithmDecision,
) -> None:
    result = run_algorithm(sample, ALGORITHMS["even-zeroes"])

    assert result.decision is expected_decision
    assert result.positivity == pytest.approx(expected_positivity)
    assert result.positive_cells_count == expected_count


def test_even_zeroes_should_reject_empty_sample() -> None:
    with pytest.raises(ValueError, match="Sample is empty"):
        run_algorithm([], ALGORITHMS["even-zeroes"])


@pytest.mark.parametrize(
    ("sample", "expected_count", "expected_positivity", "expected_decision"),
    [
        pytest.param(SAMPLE_C, 2, 0.2, AlgorithmDecision.NEGATIVE, id="sample_c"),
        pytest.param(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            0,
            0,
            AlgorithmDecision.NEGATIVE,
            id="all_0",
        ),
        pytest.param(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            11,
            11 / 12,
            AlgorithmDecision.POSITIVE,
            id="all_1",
        ),
        pytest.param(
            [1, 1],
            1,
            0.5,
            AlgorithmDecision.POSITIVE,
            id="all_1_minimum",
        ),
        pytest.param([0], 0, 0, AlgorithmDecision.NEGATIVE, id="only_one_0"),
        pytest.param([1], 0, 0, AlgorithmDecision.NEGATIVE, id="only_one_1"),
        pytest.param(
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            0,
            0,
            AlgorithmDecision.NEGATIVE,
            id="no_adjacents",
        ),
        pytest.param(
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            3,
            3 / 14,
            AlgorithmDecision.POSITIVE,
            id="above_20_percent",
        ),
    ],
)
def test_contiguous_ones(
    sample: Sample,
    expected_count: int,
    expected_positivity: float,
    expected_decision: AlgorithmDecision,
) -> None:
    result = run_algorithm(sample, ALGORITHMS["contiguous-ones"])

    assert result.decision is expected_decision
    assert result.positivity == pytest.approx(expected_positivity)
    assert result.positive_cells_count == expected_count


def test_contiguous_ones_should_reject_empty_sample() -> None:
    with pytest.raises(ValueError, match="Sample is empty"):
        run_algorithm([], ALGORITHMS["contiguous-ones"])


@pytest.mark.parametrize(
    ("sample", "expected_count", "expected_positivity", "expected_decision"),
    [
        pytest.param(SAMPLE_C, 2, 0.2, AlgorithmDecision.POSITIVE, id="sample_c"),
        pytest.param(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            0,
            0,
            AlgorithmDecision.NEGATIVE,
            id="all_0",
        ),
        pytest.param(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            0,
            0,
            AlgorithmDecision.NEGATIVE,
            id="all_1",
        ),
        pytest.param(
            [0, 1],
            0,
            0,
            AlgorithmDecision.NEGATIVE,
            id="only_previous_0",
        ),
        pytest.param(
            [1, 0],
            0,
            0,
            AlgorithmDecision.NEGATIVE,
            id="only_next_0",
        ),
        pytest.param(
            [0, 1, 0], 1, 1 / 3, AlgorithmDecision.POSITIVE, id="surrounded_minimum"
        ),
        pytest.param(
            [0, 1, 0, 1], 1, 1 / 4, AlgorithmDecision.POSITIVE, id="surrounded_not_last"
        ),
        pytest.param([0], 0, 0, AlgorithmDecision.NEGATIVE, id="only_one_0"),
        pytest.param([1], 0, 0, AlgorithmDecision.NEGATIVE, id="only_one_1"),
        pytest.param(
            [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
            0,
            0,
            AlgorithmDecision.NEGATIVE,
            id="no_surrounded",
        ),
        pytest.param(
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            1,
            0.1,
            AlgorithmDecision.NEGATIVE,
            id="exact_10_percent",
        ),
        pytest.param(
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            1,
            1 / 9,
            AlgorithmDecision.POSITIVE,
            id="above_10_percent",
        ),
    ],
)
def test_surrounded_ones(
    sample: Sample,
    expected_count: int,
    expected_positivity: float,
    expected_decision: AlgorithmDecision,
) -> None:
    result = run_algorithm(sample, ALGORITHMS["surrounded-ones"])

    assert result.decision is expected_decision
    assert result.positivity == pytest.approx(expected_positivity)
    assert result.positive_cells_count == expected_count


def test_surrounded_ones_should_reject_empty_sample() -> None:
    with pytest.raises(ValueError, match="Sample is empty"):
        run_algorithm([], ALGORITHMS["surrounded-ones"])

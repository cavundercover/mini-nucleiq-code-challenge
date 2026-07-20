from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum

from mini_nucleiq.samples import Sample


class AlgorithmDecision(StrEnum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"


@dataclass(frozen=True)
class AlgorithmResult:
    decision: AlgorithmDecision
    positivity: float
    positive_cells_count: int


def even_zeroes(sample: Sample) -> int:
    count = 0
    for index, cell in enumerate(sample):
        if index % 2 == 0 and cell == 0:
            count += 1
    return count


def contiguous_ones(sample: Sample) -> int:
    count = 0
    previous = 0
    for cell in sample:
        if cell == 1 and previous == 1:
            count += 1
        previous = cell
    return count


def surrounded_ones(sample: Sample) -> int:
    total = len(sample)
    count = 0
    for index, cell in enumerate(sample):
        if (
            cell == 1
            and index > 0
            and sample[index - 1] == 0
            and index + 1 < total
            and sample[index + 1] == 0
        ):
            count += 1
    return count


type AlgorithmStrategy = Callable[[Sample], int]


@dataclass(frozen=True)
class Algorithm:
    strategy: AlgorithmStrategy
    positivity_threshold: int


ALGORITHMS = {
    "even-zeroes": Algorithm(strategy=even_zeroes, positivity_threshold=30),
    "contiguous-ones": Algorithm(strategy=contiguous_ones, positivity_threshold=20),
    "surrounded-ones": Algorithm(strategy=surrounded_ones, positivity_threshold=10),
}


def run_algorithm(sample: Sample, algorithm: Algorithm) -> AlgorithmResult:
    total = len(sample)
    if len(sample) == 0:
        raise ValueError("Sample is empty")
    count = algorithm.strategy(sample)
    decision = (
        AlgorithmDecision.POSITIVE
        if (count * 100 > algorithm.positivity_threshold * total)
        else AlgorithmDecision.NEGATIVE
    )
    return AlgorithmResult(
        decision=decision, positivity=count / total, positive_cells_count=count
    )

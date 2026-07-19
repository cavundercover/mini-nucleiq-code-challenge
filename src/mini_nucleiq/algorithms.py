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


def even_zeroes(sample: Sample) -> AlgorithmResult:
    total = len(sample)
    count = 0
    if total == 0:
        raise ValueError("Sample is empty")
    for index, cell in enumerate(sample):
        if index % 2 == 0 and cell == 0:
            count += 1
    decision = (
        AlgorithmDecision.POSITIVE
        if (count * 100 > 30 * total)
        else AlgorithmDecision.NEGATIVE
    )
    return AlgorithmResult(
        decision=decision, positivity=count / total, positive_cells_count=count
    )

from dataclasses import dataclass
from enum import StrEnum

from mini_nucleiq import samples


class AnalysisDecision(StrEnum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"


@dataclass(frozen=True)
class AnalysisResult:
    decision: AnalysisDecision


def analyze_sample(
    sample_name: str, algorithms: list[str], samples_client: samples.SamplesClient
) -> AnalysisResult:
    raise NotImplementedError

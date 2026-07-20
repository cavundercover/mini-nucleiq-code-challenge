from dataclasses import dataclass
from enum import StrEnum

from mini_nucleiq import samples
from mini_nucleiq.algorithms import (
    ALGORITHMS,
    AlgorithmDecision,
    run_algorithm,
)


class AnalysisDecision(StrEnum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"


@dataclass(frozen=True)
class AnalysisResult:
    decision: AnalysisDecision


def analyze_sample(
    sample_name: str, algorithms: list[str], samples_client: samples.SamplesClient
) -> AnalysisResult:
    sample = samples_client.get_sample(sample_name=sample_name)
    algorithm_results = []
    for name in algorithms:
        algorithm_results.append(run_algorithm(sample, ALGORITHMS[name]))
    positives = 0
    for result in algorithm_results:
        if result.decision is AlgorithmDecision.POSITIVE:
            positives += 1
    decision = (
        AnalysisDecision.POSITIVE
        if positives * 2 > len(algorithms)
        else AnalysisDecision.NEGATIVE
    )
    return AnalysisResult(decision=decision)

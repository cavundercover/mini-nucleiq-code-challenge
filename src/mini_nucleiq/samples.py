from typing import Protocol

type Sample = list[int]


class SamplesClient(Protocol):
    def get_sample(self, sample_name: str) -> Sample:
        """Return cell data of a sample named by sample_name"""

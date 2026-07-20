from typing import Protocol

import httpx

type Sample = list[int]


class SamplesClient(Protocol):
    def get_sample(self, sample_name: str) -> Sample:
        """Return cell data of a sample named by sample_name"""

class HttpSamplesClient:
    BASE_URL = "https://raw.githubusercontent.com/cellsia/mini-nucleiq-code-challenge/main/samples"

    def get_sample(self, sample_name: str) -> Sample:
        response = httpx.get(f"{self.BASE_URL}/{sample_name}.json")
        response.raise_for_status()
        sample: Sample = response.json()["cells"]
        return sample
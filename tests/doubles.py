from mini_nucleiq import samples


class StubSamplesClient:
    def __init__(self, sample: samples.Sample) -> None:
        self._sample = sample

    def get_sample(self, sample_name: str) -> samples.Sample:
        return self._sample

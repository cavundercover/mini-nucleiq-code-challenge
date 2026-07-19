import pytest

from mini_nucleiq.samples import Sample

SAMPLE_C: Sample = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1]


@pytest.fixture
def sample_c() -> Sample:
    return SAMPLE_C

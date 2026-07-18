import pytest

from mini_nucleiq import samples


@pytest.fixture
def sample_c() -> samples.Sample:
    return [0, 0, 1, 0, 0, 1, 0, 1, 1, 1]

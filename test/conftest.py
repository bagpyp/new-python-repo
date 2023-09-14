import pytest

from src.config.properties import initialize


@pytest.fixture(scope="session", autouse=True)
def initialized_properties():
    initialize()

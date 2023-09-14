from src.config.properties import properties


def test_properties():
    assert "KEY" in properties

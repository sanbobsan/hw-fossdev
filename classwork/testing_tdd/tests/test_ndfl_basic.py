from ndfl.main import calculate_ndfl_tax


def test_ndfl():
    assert calculate_ndfl_tax() is None

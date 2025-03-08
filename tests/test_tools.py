from lib.tools import generate_depths


def test_depth_generation():
    """Test."""
    assert generate_depths([2, 5]) == [2, 3, 4, 5, 4, 3]

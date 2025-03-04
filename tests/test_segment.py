from lib.segment import Segment


def test_segment():
    """Test."""
    seg = Segment(start=(10, 10), length=10, angle=0)
    assert seg.end == (20, 10)

    seg.angle = 90
    assert seg.end == (10, 20)

    seg.angle = 180
    assert seg.end == (0, 10)

    seg.angle = 270
    assert seg.end == (10, 0)

from lib.curves.hilbert import Hilbert


def test_hilbert():
    """Test."""
    hilb = Hilbert()

    hilb.depth_index = 1
    assert round(hilb.segment_length, 3) == 56.667

    hilb.depth_index = 3
    assert round(hilb.hue_increment, 9) == 0.003921569

    hilb.depth_index = 4
    assert round(hilb.hue_increment, 9) == 0.000977517

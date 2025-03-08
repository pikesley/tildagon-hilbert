from lib.curves.hilbert_ii import HilbertII


def test_hilbert_ii():
    """Test."""
    hilb = HilbertII()

    hilb.depth_index = 0
    assert hilb.segment_length == 85

    hilb.depth_index = 1
    assert hilb.segment_length == 21.25

    hilb.depth_index = 2
    assert round(hilb.segment_length, 9) == 6.538461538

    hilb.depth_index = 3
    assert hilb.segment_length == 2.125

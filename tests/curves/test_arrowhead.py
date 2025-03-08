from lib.curves.arrowhead import Arrowhead


def test_arrowhead():
    """Test."""
    ah = Arrowhead()

    ah.depth_index = 0
    assert ah.segment_length == 50

    ah.depth_index = 1
    assert ah.segment_length == 25

    ah.depth_index = 2
    assert ah.segment_length == 12.5

    ah.depth_index = 2
    assert ah.hue_increment == 0.0125

    ah.depth_index = 3
    assert round(ah.hue_increment, 9) == 0.004132231

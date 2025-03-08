from lib.curves.square import Square


def test_square():
    """Test."""
    sq = Square()

    sq.depth_index = 0
    assert round(sq.segment_length, 2) == 47.6

    sq.depth_index = 1
    assert round(sq.segment_length, 2) == 18.31

    sq.depth_index = 2
    assert round(sq.segment_length, 2) == 8.21

    sq.depth_index = 3
    assert round(sq.segment_length, 2) == 3.9

    sq.depth_index = 0
    assert sq.hue_increment == 1 / 20

    sq.depth_index = 1
    assert sq.hue_increment == 1 / 84

    sq.depth_index = 2
    assert sq.hue_increment == 1 / 340

    sq.depth_index = 3
    assert sq.hue_increment == 1 / 1364

    sq.depth_index = 4
    assert sq.hue_increment == 1 / 5640

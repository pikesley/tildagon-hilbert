from lib.curves.peano_gosper import PeanoGosper


def test_peano_gosper():
    """Test."""
    pg = PeanoGosper()

    pg.depth_index = 0
    assert round(pg.segment_length, 9) == 29.850746269

    pg.depth_index = 1
    assert round(pg.segment_length, 9) == 9.87654321

    pg.depth_index = 2
    assert round(pg.segment_length, 9) == 3.80952381

    pg.depth_index = 0
    assert round(pg.hue_increment, 9) == 0.020833333

    pg.depth_index = 1
    assert round(pg.hue_increment, 9) == 0.002923977

    pg.depth_index = 2
    assert round(pg.hue_increment, 9) == 0.000416667

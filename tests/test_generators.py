from lib.conf import conf
from lib.generators import construct_string, iterate


def test_iterate_hilbert():
    """Test."""
    assert "".join(list(iterate("f", conf["hilbert"]["rules"]))) == "f"
    assert "".join(list(iterate("a", conf["hilbert"]["rules"]))) == "+bf-afa-fb+"
    assert "".join(list(iterate("b", conf["hilbert"]["rules"]))) == "-af+bfb+fa-"
    assert (
        "".join(list(iterate("+bf-a", conf["hilbert"]["rules"])))
        == "+-af+bfb+fa-f-+bf-afa-fb+"
    )
    assert "".join(list(iterate("xyz", conf["hilbert"]["rules"]))) == "xyz"


def test_iterate_arrowhead():
    """Test."""
    assert "".join(list(iterate("f", conf["arrowhead"]["rules"]))) == "f"
    assert "".join(list(iterate("a", conf["arrowhead"]["rules"]))) == "bf+af+b"
    assert (
        "".join(list(iterate("bf+af+b", conf["arrowhead"]["rules"])))
        == "af-bf-af+bf+af+bf+af-bf-a"
    )


def test_construct_string():
    """Test."""
    assert (
        "".join(list(construct_string("a", conf["hilbert"]["rules"], 1)))
        == "+bf-afa-fb+"
    )
    assert "".join(list(construct_string("a", conf["hilbert"]["rules"], 3))) == (
        "+-+bf-afa-fb+f+-af+bfb+fa-f-af+bfb+fa-+f+bf-afa-fb+-f-+-af+bfb+fa-f-+bf-"
        "afa-fb+f+bf-afa-fb+-f-af+bfb+fa-+f+-af+bfb+fa-f-+bf-afa-fb+f+bf-afa-fb+-"
        "f-af+bfb+fa-+-f-+bf-afa-fb+f+-af+bfb+fa-f-af+bfb+fa-+f+bf-afa-fb+-+"
    )

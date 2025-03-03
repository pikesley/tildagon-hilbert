from lib.hilbert import construct_string, iterate_hilbert


def test_iterate_hilbert():
    """Test."""
    assert iterate_hilbert("f") == "f"
    assert iterate_hilbert("a") == "+bf-afa-fb+"
    assert iterate_hilbert("b") == "-af+bfb+fa-"
    assert iterate_hilbert("+bf-a") == "+-af+bfb+fa-f-+bf-afa-fb+"
    assert iterate_hilbert("xyz") == "xyz"


def test_construct_string():
    """Test."""
    assert construct_string("a", 1) == "+bf-afa-fb+"
    assert construct_string("a", 3) == (
        "+-+bf-afa-fb+f+-af+bfb+fa-f-af+bfb+fa-+f+bf-afa-fb+-f-+-af+bfb+fa-f-+bf-"
        "afa-fb+f+bf-afa-fb+-f-af+bfb+fa-+f+-af+bfb+fa-f-+bf-afa-fb+f+bf-afa-fb+-"
        "f-af+bfb+fa-+-f-+bf-afa-fb+f+-af+bfb+fa-f-af+bfb+fa-+f+bf-afa-fb+-+"
    )

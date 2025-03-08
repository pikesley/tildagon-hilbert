from lib.curves.hilbert import Hilbert

# def test_iterate_hilbert():
#     """Test."""
#     assert "".join(list(iterate("f", curves["hilbert"]["rules"]))) == "f"
#     assert "".join(list(iterate("a", curves["hilbert"]["rules"]))) == "+bf-afa-fb+"
#     assert "".join(list(iterate("b", curves["hilbert"]["rules"]))) == "-af+bfb+fa-"
#     assert (
#         "".join(list(iterate("+bf-a", curves["hilbert"]["rules"])))
#         == "+-af+bfb+fa-f-+bf-afa-fb+"
#     )
#     assert "".join(list(iterate("xyz", curves["hilbert"]["rules"]))) == "xyz"


# def test_iterate_arrowhead():
#     """Test."""
#     assert "".join(list(iterate("f", curves["arrowhead"]["rules"]))) == "f"
#     assert "".join(list(iterate("a", curves["arrowhead"]["rules"]))) == "bf+af+b"
#     assert (
#         "".join(list(iterate("bf+af+b", curves["arrowhead"]["rules"])))
#         == "af-bf-af+bf+af+bf+af-bf-a"
#     )


def test_construct_string():
    """Test."""
    hilb = Hilbert()

    hilb.depth_index = 0
    assert "".join(list(hilb.string)) == "+bf-afa-fb+"

    hilb.depth_index = 2
    assert "".join(list(hilb.string)) == (
        "+-+bf-afa-fb+f+-af+bfb+fa-f-af+bfb+fa-+f+bf-afa-fb+-f-+-af+bfb+fa-f-+bf-"
        "afa-fb+f+bf-afa-fb+-f-af+bfb+fa-+f+-af+bfb+fa-f-+bf-afa-fb+f+bf-afa-fb+-"
        "f-af+bfb+fa-+-f-+bf-afa-fb+f+-af+bfb+fa-f-af+bfb+fa-+f+bf-afa-fb+-+"
    )

from lib.arrowhead import iterate_arrowhead


def test_iterate_arrowhead():
    """Test."""
    assert "".join(list(iterate_arrowhead("f"))) == "f"
    assert "".join(list(iterate_arrowhead("a"))) == "bf+af+b"
    assert "".join(list(iterate_arrowhead("bf+af+b"))) == "af-bf-af+bf+af+bf+af-bf-a"

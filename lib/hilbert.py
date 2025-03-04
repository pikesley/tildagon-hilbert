# https://medium.com/@gregking917/the-hilbert-curve-21d7e9b2789c


def iterate_hilbert(start_string):
    """Iterate."""
    rules = {"a": "+bf-afa-fb+", "b": "-af+bfb+fa-"}
    new_string = ""

    for char in start_string:
        new_string = new_string + rules[char] if char in rules else new_string + char

    for char in new_string:
        yield char


# TODO make these both generators
def construct_string(start_hilbert, iterations):
    """Construct a whole string."""
    cur_hilbert = start_hilbert

    for _ in range(iterations):
        cur_hilbert = iterate_hilbert(cur_hilbert)

    yield from cur_hilbert

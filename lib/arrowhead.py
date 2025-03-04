def iterate_arrowhead(start_string):
    """Iterate."""
    rules = {"a": "bf+af+b", "b": "af-bf-a"}
    new_string = ""

    for char in start_string:
        new_string = new_string + rules[char] if char in rules else new_string + char

    for char in new_string:
        yield char


def construct_arrowhead_string(start_arrowhead, iterations):
    """Construct a whole string."""
    cur_arrowhead = start_arrowhead

    for _ in range(iterations):
        cur_arrowhead = iterate_arrowhead(cur_arrowhead)

    yield from cur_arrowhead

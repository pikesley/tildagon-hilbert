def iterate(start_string, rules):
    """Iterate."""
    new_string = ""

    for char in start_string:
        new_string = new_string + rules[char] if char in rules else new_string + char

    for char in new_string:
        yield char


def construct_string(start_string, rules, iterations):
    """Construct string."""
    cur_string = start_string

    for _ in range(iterations):
        cur_string = iterate(cur_string, rules)

    yield from cur_string

def hilbert_segment_length(screen_size, depth):
    """Calculate segment length."""
    return screen_size / ((2**depth) - 1)


def arrowhead_segment_length(screen_size, depth):
    """Calculate segment length."""
    return screen_size / (2**depth)  # TODO still a bit guessy


def hilbert_hue_increment(depth):
    """Calculate hue-increment."""
    return 1.0 / (2 ** (depth * 2) - 1)


def arrowhead_hue_increment(depth):
    """Calculate hue-increment."""
    return 1.0 / (2 ** (depth * 2) - 1)  # TODO this is bogus

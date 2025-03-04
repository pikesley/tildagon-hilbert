def hilbert_segment_length(start_point, depth):
    """Calculate segment length."""
    return abs(start_point) * 2 / ((2**depth) - 1)


def arrowhead_segment_length(start_point, depth):
    """Calculate segment length."""
    return (abs(start_point) * 2) / 2**depth


def hilbert_hue_increment(depth):
    """Calculate hue-increment."""
    return 1.0 / (2 ** (depth * 2) - 1)


def arrowhead_hue_increment(depth):
    """Calculate hue-increment."""
    return 1.0 / (2 ** (depth * 2) - 1)  # TODO this is bogus

def generate_depths(depth_range):
    """Generate a depth-set."""
    up = list(range(*depth_range)) + [depth_range[-1]]
    down = list(reversed(up))[1:-1]

    return up + down

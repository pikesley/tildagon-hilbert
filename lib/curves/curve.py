from ..generators import generate_string
from ..tools import generate_depths


class Curve:
    """A Curve."""

    def __init__(self):
        """Construct."""
        self.configure()

        self.set_depths()
        self.depth_index = 0

    def set_depths(self):
        """Set depths."""
        self.depths = generate_depths(self.depth_range)

    def next_depth(self):
        """Next depth."""
        self.depth_index = (self.depth_index + 1) % len(self.depths)

    @property
    def depth(self):
        """Current depth."""
        return self.depths[self.depth_index]

    @property
    def string(self):
        """The string."""
        return generate_string(self.seed, self.rules, self.depth)

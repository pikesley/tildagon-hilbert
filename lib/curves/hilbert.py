from .curve import Curve


class Hilbert(Curve):
    """A Hilbert Curve."""

    def configure(self):
        """Configure."""
        self.rules = {"a": "+bf-afa-fb+", "b": "-af+bfb+fa-"}
        self.seed = "a"
        self.angle = 90

        self.depth_range = [1, 6]
        self.start_point = (-85, -85)

    @property
    def segment_length(self):
        """Segment length."""
        return (85 * 2) / ((2**self.depth) - 1)

    @property
    def hue_increment(self):
        """Hue-increment."""
        return 1.0 / ((2 ** (self.depth * 2)) - 1)

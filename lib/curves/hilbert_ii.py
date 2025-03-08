from .curve import Curve


class HilbertII(Curve):
    """A different Hilbert Curve."""

    def configure(self):
        """Configure."""
        self.rules = {"a": "afbfa+f+bfafb-f-afbfa", "b": "bfafb-f-afbfa+f+bfafb"}
        self.seed = "a"
        self.angle = 90

        self.depth_range = [1, 4]
        self.start_point = (-85, -85)

    @property
    def segment_length(self):
        """Segment length."""
        deniminators = {
            1: 1,
            2: 4,
            3: 13,
            4: 40,
        }
        return 85 / deniminators[self.depth]

    @property
    def hue_increment(self):
        """Hue-increment."""
        increments = {1: 8, 2: 80, 3: 728, 4: 6560}
        return 1.0 / increments[self.depth]

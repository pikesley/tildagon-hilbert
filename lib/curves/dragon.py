from .curve import Curve


class Dragon(Curve):
    """A Dragon Curve."""

    def configure(self):
        """Configure."""
        self.rules = {"a": "a+bf+", "b": "-fa-b"}
        self.seed = "fa"
        self.angle = 90

        self.depth_range = [1, 9]
        self.half_side = 85

    @property
    def start_point(self):
        """Start point."""
        factors = {
            1: (-0.5, -0.5),
            2: (-0.5, -1.0),
            3: (0.5, -1.0),
            4: (1.5, -0.5),
            5: (2, 1.5),
            6: (1.5, 3.5),
            7: (-2.5, 4),
            8: (-6.5, 2.5),
            9: (-6.5, -7),
        }

        try:
            return [self.segment_length * factor for factor in factors[self.depth]]
        except KeyError:
            return (0, 0)

    @property
    def segment_length(self):
        """Segment length."""
        side = self.half_side * 2
        values = {
            1: side,
            2: side / 3,
            3: side / 3,
            4: side / 5,
            5: side / 7,
            6: side / 11,
            7: side / 15,
            8: side / 20,
            9: side / 31,
        }

        try:
            return values[self.depth]
        except KeyError:
            return 1

    @property
    def hue_increment(self):
        """Hue-increment."""
        return 1.0 / 2**self.depth

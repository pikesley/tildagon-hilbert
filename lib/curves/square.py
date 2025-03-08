from .curve import Curve


class Square(Curve):
    """A Square Curve."""

    def configure(self):
        """Configure."""
        self.rules = {"a": "af-f+f-af+f+af-f+f-a"}
        self.seed = "f+af+f+af"
        self.angle = 90

        self.depth_range = [1, 5]

    @property
    def start_point(self):
        """Start-point."""
        return (-self.segment_length / 2, -119)

    @property
    def segment_length(self):
        """Segment length."""
        return 238 / (2 ** (self.depth + 2) - 3)

    @property
    def hue_increment(self):
        """Hue-increment."""
        denonimators = {
            1: 20,
            2: 84,
            3: 340,
            4: 1364,
            5: 5640,
        }
        return 1.0 / denonimators[self.depth]

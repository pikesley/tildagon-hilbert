from .curve import Curve


class Arrowhead(Curve):
    """A Sierpinski Arrowhead Curve."""

    def configure(self):
        """Configure."""
        self.rules = {"a": "bf+af+b", "b": "af-bf-a"}
        self.seed = "bf"
        self.angle = 60

        self.depth_range = [2, 6]

    @property
    def start_point(self):
        """Start-point."""
        y = 60
        if self.depth % 2 == 0:
            y = -60

        return (-100, y)

    @property
    def segment_length(self):
        """Segment length."""
        # TODO unhardcode this `100``
        return (100 * 2) / 2**self.depth

    @property
    def hue_increment(self):
        """Hue-increment."""
        return 1.0 / ((3**self.depth) - 1)

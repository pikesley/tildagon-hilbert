from .curve import Curve


class PeanoGosper(Curve):
    """A Peano-Gosper Curve."""

    def configure(self):
        """Configure."""
        self.rules = {"a": "a+bf++bf-fa--fafa-bf+", "b": "-fa+bfbf++bf+fa--fa-b"}
        self.seed = "fa"
        self.angle = 60

        self.depth_range = [2, 4]

    @property
    def start_point(self):
        """Start point."""
        values = {2: (-50, -104), 3: (-10, -103), 4: (30, -102)}

        try:
            return values[self.depth]
        except KeyError:
            return (0, 0)

    @property
    def segment_length(self):
        """Segment length."""
        values = {
            1: 80,
            2: 29.850746269,
            3: 9.87654321,
            4: 3.80952381,
        }
        return values[self.depth]

    @property
    def hue_increment(self):
        """Hue-increment."""
        return 1.0 / ((7**self.depth) - 1)

from .curve import Curve


class Koch(Curve):
    """A Koch Curve."""

    def configure(self):
        """Configure."""
        self.rules = {"f": " f-f+f+fff-f-f+f"}
        self.seed = "f"
        self.angle = 60

        self.depth_range = [1, 4]
        self.start_point = (0, 0)

    @property
    def segment_length(self):
        """Segment length."""
        return 0.1

    @property
    def hue_increment(self):
        """Hue-increment."""
        increments = {1: 8, 2: 80, 3: 728, 4: 6560}
        return 1.0 / increments[self.depth]

try:
    from ..common.rgb_from_hue import rgb_from_hue
except ImportError:
    from common.colour_tools import rgb_from_hue

from math import cos, radians, sin


class Segment:
    """A line."""

    def __init__(self, start=(0, 0), length=0, angle=0, hue=1.0):
        """Construct."""
        self.start = start
        self.length = length
        self.angle = angle
        self.hue = hue
        self.colour = rgb_from_hue(self.hue)

    @property
    def end(self):
        """Locate our end-point."""
        return (
            round(self.start[0] + (cos(radians(self.angle)) * self.length), 10),
            round(self.start[1] + (sin(radians(self.angle)) * self.length), 10),
        )

    def draw(self, ctx):
        """Draw."""
        ctx.rgb(*self.colour)

        ctx.move_to(*self.start)
        ctx.line_to(*self.end)

        ctx.stroke()

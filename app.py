
from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .lib.background import Background
from .lib.hilbert import construct_string
from .pikesley.vector.vector import Vector


class Hilbert(app.App):
    """Hilbert."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.angle = 90
        self.depth = 4
        self.string = construct_string("a", self.depth)
        self.index = 0

        self.size = 150
        self.segment_length = self.size / ((2**self.depth) - 1)

    def update(self, _):
        """Update."""
        self.scan_buttons()
        self.portion = self.string[:]
        # self.index += 8

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))
        self.draw_overlays(ctx)

        ctx.rgb(255, 0, 0)
        ctx.move_to(-(self.size / 2), -(self.size / 2))
        self.v = Vector(self.segment_length, 0)
        for char in self.portion:
            if char == "+":
                self.v.rotate(self.angle)
            if char == "-":
                self.v.rotate(-self.angle)
            if char == "f":
                ctx.rel_line_to(*self.v.coords)

        ctx.stroke()

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()


__app_export__ = Hilbert


from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from math import radians
import app

from .lib.background import Background
from .pikesley.vector.vector import Vector
from .lib.hilbert import construct_string

class Hilbert(app.App):
    """Hilbert."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.blanked = False
        self.v = Vector(10, 0)

    def update(self, _):
        """Update."""
        self.scan_buttons()

        self.string = construct_string("a", 3)

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        if not self.blanked:
            self.overlays.append(Background(colour=(0, 0, 0)))
            self.draw_overlays(ctx)
            self.blanked = True

        ctx.rgb(255, 0, 0)
        ctx.move_to(0, 0)
        for char in self.string:
            if char == "+":
                v.rotate(90)
            if char == "-":
                v.rotate(-90)
            if char == "f":
                ctx.rel_line_to(*v.coords)



        ctx.stroke()


    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()


__app_export__ = Hilbert

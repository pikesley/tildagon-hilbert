# https://www.robertdickau.com/lsys2d.html
# https://medium.com/@gregking917/the-hilbert-curve-21d7e9b2789c

from math import radians, sqrt
from random import random

from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from tildagonos import tildagonos

import app

from .lib.background import Background
from .lib.curve_list import curves
from .lib.gamma import gamma_corrections
from .lib.segment import Segment
from .pikesley.rgb_from_hue.rgb_from_hue import rgb_from_hue
from .pikesley.shapes.circle import Circle
from .pikesley.shapes.hexagon import Hexagon


class Fractals(app.App):
    """Fractal curves."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)

        self.curve_index = 0
        self.curve = curves[self.curve_index]()
        self.reset()

    def reset(self):
        """Reset."""
        self.string = self.curve.string
        self.angle = 0

        self.blanked = False
        self.segment = None
        self.hue = random()
        self.rotation = random() * radians(360)

    def update(self, _):
        """Update."""
        self.scan_buttons()

        self.segment_generated = False
        while not self.segment_generated:
            try:
                self.process_char(next(self.string))

            except StopIteration:
                self.curve.next_depth()
                self.reset()

        self.hue += self.curve.hue_increment
        self.light_leds()

    def process_char(self, char):
        """Process a char."""
        if char == "+":
            self.angle = (self.angle + self.curve.angle) % 360
        if char == "-":
            self.angle = (self.angle - self.curve.angle) % 360

        if char == "f":
            self.segment = Segment(
                start=self.get_start_point,
                length=self.curve.segment_length,
                angle=self.angle,
                hue=self.hue,
            )
            self.segment_generated = True

    @property
    def get_start_point(self):
        """Where to start the next segment."""
        if self.segment:
            return self.segment.end

        return self.curve.start_point

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        ctx.rotate(self.rotation)

        if not self.blanked:
            self.overlays.append(Background(colour=(0, 0, 0)))
            # self.draw_helpers(type="hexagons")
            self.blanked = True

        if self.segment:
            self.overlays.append(self.segment)

        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["CONFIRM"]):
            self.button_states.clear()
            self.curve_index = (self.curve_index + 1) % len(curves)
            self.curve = curves[self.curve_index]()
            self.reset()

    def light_leds(self):
        """Light lights."""
        brightness = 0.5

        colour = [
            gamma_corrections[int(c * brightness * 255)] for c in rgb_from_hue(self.hue)
        ]

        for index in range(12):
            tildagonos.leds[index + 1] = colour

        tildagonos.leds.write()

    def draw_helpers(self, variety):
        """Draw some framework."""
        colour = (0.3, 0.3, 0.3)
        if variety == "circles":
            for i in range(0, 140, 23):
                self.overlays.append(
                    Circle(centre=(0, 0), size=i, colour=colour, filled=False)
                )

        if variety == "hexagons":
            size = 40
            self.overlays.append(
                Hexagon(centre=(0, 0), size=size, colour=colour, filled=False)
            )
            self.overlays.append(
                Hexagon(
                    centre=(0, size * sqrt(3)), size=size, colour=colour, filled=False
                )
            )
            self.overlays.append(
                Hexagon(
                    centre=(0, -size * sqrt(3)), size=size, colour=colour, filled=False
                )
            )


__app_export__ = Fractals

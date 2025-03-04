from math import radians
from random import random

from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from tildagonos import tildagonos

import app

from .lib.background import Background
from .lib.conf import conf
from .lib.gamma import gamma_corrections
from .lib.generators import construct_string
from .lib.segment import Segment
from .pikesley.rgb_from_hue.rgb_from_hue import rgb_from_hue

curve = "arrowhead"


class Hilbert(app.App):
    """Hilbert."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.screen_size = conf[curve]["screen-size"]

        self.depths = list(range(1, conf[curve]["max-depth"] + 1)) + list(
            range(conf[curve]["max-depth"] - 1, 1, -1)
        )
        self.reset()

    def reset(self):
        """Reset."""
        depth = self.depths[0]
        start_letter = conf[curve]["start-letter"][depth % 2]
        self.string = construct_string(start_letter, conf[curve]["rules"], depth)
        self.hue_increment = conf[curve]["hue-increment"](depth)
        self.segment_length = conf[curve]["segment-length"](self.screen_size, depth)
        self.angle = 0

        self.blanked = False
        self.segment = None
        self.hue = random()
        self.hue = 0
        self.rotation = random() * radians(360)

    def rotate_depths(self):
        """Rotate `depths` list."""
        self.depths = self.depths[1:] + [self.depths[0]]

    def update(self, _):
        """Update."""
        self.scan_buttons()

        found_an_f = False

        while not found_an_f:
            try:
                start_point = (-(self.screen_size / 2), -(self.screen_size / 2))
                if self.segment:
                    start_point = self.segment.end

                char = next(self.string)
                if char == "+":
                    self.angle = (self.angle + conf[curve]["angle"]) % 360
                if char == "-":
                    self.angle = (self.angle - conf[curve]["angle"]) % 360

                if char == "f":
                    found_an_f = True
                    self.segment = Segment(
                        start=start_point,
                        length=self.segment_length,
                        angle=self.angle,
                        hue=self.hue,
                    )
                    self.hue += self.hue_increment

            except StopIteration:
                self.rotate_depths()
                self.reset()

        self.light_leds()

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        ctx.rotate(self.rotation)

        if not self.blanked:
            self.overlays.append(Background(colour=(0, 0, 0)))
            self.blanked = True

        if self.segment:
            self.overlays.append(self.segment)

        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

    def light_leds(self):
        """Light lights."""
        brightness = 0.5

        colour = [
            gamma_corrections[int(c * brightness * 255)] for c in rgb_from_hue(self.hue)
        ]

        for index in range(12):
            tildagonos.leds[index + 1] = colour

        tildagonos.leds.write()


__app_export__ = Hilbert

from .tools import (
    arrowhead_hue_increment,
    arrowhead_segment_length,
    hilbert_hue_increment,
    hilbert_segment_length,
)

conf = {
    "arrowhead": {
        "rules": {"a": "bf+af+b", "b": "af-bf-a"},
        "angle": 60,
        "max-depth": 6,
        "screen-size": 170,
        "start-point": (-100, -60),
        "start-letter": ["b", "a"],
        "segment-length": arrowhead_segment_length,
        "hue-increment": arrowhead_hue_increment,
    },
    "hilbert": {
        "rules": {"a": "+bf-afa-fb+", "b": "-af+bfb+fa-"},
        "angle": 90,
        "max-depth": 6,
        "screen-size": 170,
        "start-point": (-85, -85),
        "start-letter": ["a", "a"],  # TODO this is fuckery. might be a `% length``
        "segment-length": hilbert_segment_length,
        "hue-increment": hilbert_hue_increment,
    },
}

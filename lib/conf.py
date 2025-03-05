conf = {
    "arrowhead": {
        "rules": {"a": "bf+af+b", "b": "af-bf-a"},
        "angle": 60,
        "max-depth": 6,
        "start-point": (-100, -60),
        "start-letters": ["b", "a"],
        "segment-length": (
            lambda depth: (abs(conf["arrowhead"]["start-point"][0]) * 2)
            / ((2**depth) - 1)
        ),
        "hue-increment": (lambda depth: 1.0 / (3**depth)),
    },
    "hilbert": {
        "rules": {"a": "+bf-afa-fb+", "b": "-af+bfb+fa-"},
        "angle": 90,
        "max-depth": 6,
        "start-point": (-85, -85),
        "start-letters": ["a"],
        "segment-length": (
            lambda depth: (abs(conf["hilbert"]["start-point"][0]) * 2)
            / ((2**depth) - 1)
        ),
        "hue-increment": (lambda depth: 1.0 / (2 ** (depth * 2)) - 1),
    },
    # "koch": {
    #     "rules": {"f": " f-f+f+fff-f-f+f"},
    #     "angle": 90,
    #     "max-depth": 6,
    #     "start-point": (-50, -50),
    #     "start-letters": ["f", "f"],
    #     "segment-length": koch_segment_length,
    #     "hue-increment": hilbert_hue_increment,
    # },
    # "square": {
    #     "rules": {"a": "af-f+f-af+f+af-f+f-a"},
    #     "angle": 90,
    #     "max-depth": 6,
    #     "start-point": (-120, 0),
    #     "start-letters": ["a", "a"],
    #     "segment-length": (
    #         lambda depth: (abs(conf["square"]["start-point"][0]) * 2) /
    # ((2**depth) - 1)
    #     ),
    #     "hue-increment": (lambda depth: 1.0 / (2 ** (depth * 2)) - 1),
    # },
}

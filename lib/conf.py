from collections import OrderedDict


def peano_gosper_segment_length(depth):
    """Segment length."""
    values = {
        1: 80,
        2: 29.850746269,
        3: 9.87654321,
        4: 3.80952381,
    }
    return values[depth]


def hilbert_ii_segment_length(depth):
    """Segment length."""
    deniminators = {
        1: 1,
        2: 4,
        3: 13,
        4: 40,
    }
    return 85 / deniminators[depth]


def hilbert_ii_hue_increment(depth):
    """Hue-increment."""
    increments = {1: 8, 2: 80, 3: 728, 4: 6560}
    return 1.0 / increments[depth]


def square_segment_length(depth):
    """Segment length."""
    return 238 / (2 ** (depth + 2) - 3)


def square_hue_increment(depth):
    """Hue-increment."""
    denonimators = {
        1: 20,
        2: 84,
        3: 340,
        4: 1364,
        5: 5640,
    }
    return 1.0 / denonimators[depth]


curves = OrderedDict(
    {
        # "hilbert": {
        #     "rules": {"a": "+bf-afa-fb+", "b": "-af+bfb+fa-"},
        #     "angle": 90,
        #     "depths": OrderedDict(
        #         {
        #             1: (-85, -85),
        #             2: (-85, -85),
        #             3: (-85, -85),
        #             4: (-85, -85),
        #             5: (-85, -85),
        #             6: (-85, -85),
        #         }
        #     ),
        #     "start-letters": ["a"],
        #     "segment-length": (lambda depth: (85 * 2) / ((2**depth) - 1)),
        #     "hue-increment": (lambda depth: 1.0 / ((2 ** (depth * 2)) - 1)),
        # },
        # "hilbert-ii": {
        #     "rules": {"a": "afbfa+f+bfafb-f-afbfa", "b": "bfafb-f-afbfa+f+bfafb"},
        #     "angle": 90,
        #     "depth-range": [1, 4],
        #     "start-point": (-85, -85),
        #     "depths": OrderedDict(
        #         {
        #             1: (-85, -85),
        #             2: (-85, -85),
        #             3: (-85, -85),
        #             4: (-85, -85),
        #         }
        #     ),
        #     "start-letters": ["a"],
        #     "segment-length": hilbert_ii_segment_length,
        #     "hue-increment": hilbert_ii_hue_increment,
        # },
        # "arrowhead": {
        #     "rules": {"a": "bf+af+b", "b": "af-bf-a"},
        #     "angle": 60,
        #     "depths": OrderedDict(
        #         {
        #             2: (-100, -60),
        #             3: (-100, -60),
        #             4: (-100, -60),
        #             5: (-100, -60),
        #             6: (-100, -60),
        #         }
        #     ),
        #     "start-letters": ["bf", "af"],
        #     "segment-length": (lambda depth: (100 * 2) / 2**depth),
        #     "hue-increment": (lambda depth: 1.0 / ((3**depth) - 1)),
        # },
        # "peano-gosper": {
        #     "rules": {"a": "a+bf++bf-fa--fafa-bf+", "b": "-fa+bfbf++bf+fa--fa-b"},
        #     "angle": 60,
        #     "start-letters": ["fa"],
        #     "depths": OrderedDict(
        #         # TODO: fix these
        #         {
        #             3: (20, -104),
        #             4: (20, -104),
        #         }
        #     ),
        #     "segment-length": peano_gosper_segment_length,
        #     "hue-increment": (lambda depth: 1.0 / ((7**depth) - 1)),
        # },
        # "square": {
        #     "rules": {"a": "af-f+f-af+f+af-f+f-a"},
        #     "angle": 90,
        #     "start-letters": ["f+af+f+af"],
        #     "segment-length": square_segment_length,
        #     "depths": OrderedDict(
        #         {
        #             1: (-square_segment_length(1) / 2, -119),
        #             2: (-square_segment_length(2) / 2, -119),
        #             3: (-square_segment_length(3) / 2, -119),
        #             4: (-square_segment_length(4) / 2, -119),
        #             5: (-square_segment_length(5) / 2, -119),
        #         }
        #     ),
        #     "hue-increment": square_hue_increment,
        # },
    }
)

# "32-segment": {
#     "rules": {"f": "-f+f-f-f+f+ff-f+f+ff+f-f-ff+ff-ff+f+f-ff-f-f+ff-f-f+f+f-f+"},
#     "angle": 90,
#     "depth-range": [2, 6],
#     "start-point": (-50, -50),
#     "start-letters": ["f"],
#     "segment-length": (lambda depth: 1),
#     "hue-increment": (lambda depth: 0),
# },
# "koch": {
#     "rules": {"f": " f-f+f+fff-f-f+f"},
#     "angle": 90,
#     "max-depth": 6,
#     "start-point": (-50, -50),
#     "start-letters": ["f", "f"],
#     "segment-length": koch_segment_length,
#     "hue-increment": hilbert_hue_increment,
# },

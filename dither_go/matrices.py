# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

from dataclasses import dataclass

from dither_go import ErrorDiffusionMatrix, OrderedDitherMatrix
from dither_go.bindings import dither


@dataclass(frozen=True)
class ErrorDiffusers:  # pylint: disable=R0902,C0103
    """
    Error diffusion matrices
    """

    Simple2D: ErrorDiffusionMatrix = dither.Simple2D()
    """Simple 2D"""

    FloydSteinberg: ErrorDiffusionMatrix = dither.FloydSteinberg()
    """Floyd-Steinberg"""

    FalseFloydSteinberg: ErrorDiffusionMatrix = dither.FalseFloydSteinberg()
    """False Floyd-Steinberg"""

    Stucki: ErrorDiffusionMatrix = dither.Stucki()
    """Stucki"""

    Burkes: ErrorDiffusionMatrix = dither.Burkes()
    """Burkes"""

    Atkinson: ErrorDiffusionMatrix = dither.Atkinson()
    """Atkinson"""

    JarvisJudiceNinke: ErrorDiffusionMatrix = dither.JarvisJudiceNinke()
    """Jarvis, Judice & Ninke"""

    Sierra: ErrorDiffusionMatrix = dither.Sierra()
    """Sierra"""

    Sierra2: ErrorDiffusionMatrix = dither.Sierra2()
    """
    Sierra2

    Sierra2 is another name for Two-Row Sierra.
    """

    Sierra2_4A: ErrorDiffusionMatrix = dither.Sierra2_4A()
    """
    Sierra2-4A

    Sierra2_4A (usually written as Sierra2-4A) is another name for Sierra Lite.
    """

    Sierra3: ErrorDiffusionMatrix = dither.Sierra3()
    """
    Sierra3

    Sierra3 is another name for the original Sierra matrix.
    """

    SierraLite: ErrorDiffusionMatrix = dither.SierraLite()
    """Sierra Lite"""

    TwoRowSierra: ErrorDiffusionMatrix = dither.TwoRowSierra()
    """Two-Row Sierra"""

    StevenPigeon: ErrorDiffusionMatrix = dither.StevenPigeon()
    """Pigeon"""


@dataclass(frozen=True)
class OrderedDitherers:  # pylint: disable=R0902,C0103
    """
    Ordered dither matrices
    """

    ClusteredDot4x4: OrderedDitherMatrix = dither.ClusteredDot4x4()
    """
    Clustered-Dot 4x4

    Comes from http://caca.zoy.org/study/part2.html
    It is not diagonal, so the dots form a grid.
    """

    ClusteredDot6x6: OrderedDitherMatrix = dither.ClusteredDot6x6()
    """
    Clustered-Dot 6x6

    Clustered-Dot 6x6 comes from Figure 5.9 of the book "Digital Halftoning" by
    Robert Ulichney. It can represent "37 levels of gray". It is not diagonal.
    """

    ClusteredDot6x6_2: OrderedDitherMatrix = dither.ClusteredDot6x6_2()
    """
    Clustered-Dot 6x6-2

    Clustered-Dot 6x6-2 comes from https://archive.is/71e9G. On the webpage it is
    called "central white point" while Clustered-Dot 6x6 is called "clustered dots".

    It is nearly identical to Clustered-Dot 6x6.
    """

    ClusteredDot6x6_3: OrderedDitherMatrix = dither.ClusteredDot6x6_3()
    """
    Clustered-Dot 6x6-3

    Clustered-Dot 6x6-3 comes from https://archive.is/71e9G. On the webpage it is
    called "balanced centered point".

    It is nearly identical to Clustered-Dot 6x6.
    """

    ClusteredDot8x8: OrderedDitherMatrix = dither.ClusteredDot8x8()
    """
    Clustered-Dot 8x8

    Clustered-Dot 8x8 comes from Figure 1.5 of the book "Modern Digital Halftoning, Second Edition",
    by Daniel L. Lau and Gonzalo R. Arce.
    It is like Clustered-Dot Diagonal 8x8, but is not diagonal. It can represent "65 gray-levels".
    """

    ClusteredDotDiagonal6x6: OrderedDitherMatrix = dither.ClusteredDotDiagonal6x6()
    """
    Clustered-Dot Diagonal 6x6

    Clustered-Dot Diagonal 6x6 comes from Figure 5.4 of the book "Digital Halftoning" by
    Robert Ulichney.
    In the book it's called ``M = 3``. It can represent "19 levels of gray".
    Its dimensions are 6x6, but as a diagonal matrix it is 7x7. It is called
    "Diagonal" because the resulting dot pattern is at a 45 degree angle.
    """

    ClusteredDotDiagonal8x8: OrderedDitherMatrix = dither.ClusteredDotDiagonal8x8()
    """
    Clustered-Dot Diagonal 8x8

    Comes from http://caca.zoy.org/study/part2.html
    They say it "mimics the halftoning techniques used by newspapers". It is called
    "Diagonal" because the resulting dot pattern is at a 45 degree angle.
    """

    ClusteredDotDiagonal8x8_2: OrderedDitherMatrix = dither.ClusteredDotDiagonal8x8_2()
    """
    Clustered-Dot Diagonal 8x8-2

    Clustered-Dot Diagonal 8x8-2 comes from Figure 5.4 of the book "Digital Halftoning" by
    Robert Ulichney.
    In the book it's called ``M = 4``. It can represent "33 levels of gray".
    Its dimensions are 8x8, but as a diagonal matrix it is 9x9. It is called
    "Diagonal" because the resulting dot pattern is at a 45 degree angle.

    It is almost identical to Clustered-Dot Diagonal 8x8, but it's worse because it can
    represent fewer gray levels. There is not much point in using it.
    """

    ClusteredDotDiagonal8x8_3: OrderedDitherMatrix = dither.ClusteredDotDiagonal8x8_3()
    """
    Clustered-Dot Diagonal 8x8-3

    Clustered-Dot Diagonal 8x8-3 comes from https://archive.is/71e9G. On the webpage
    it is called "diagonal ordered matrix with balanced centered points".

    It is almost identical to Clustered-Dot Diagonal 8x8, but worse because it can
    represent fewer gray levels. There is not much point in using it.

    It is called "Diagonal" because the resulting dot pattern is at a 45 degree angle.
    """

    ClusteredDotDiagonal16x16: OrderedDitherMatrix = dither.ClusteredDotDiagonal16x16()
    """
    Clustered-Dot Diagonal 16x16

    Clustered-Dot Diagonal 16x16 comes from Figure 5.4 of the book "Digital Halftoning" by
    Robert Ulichney.
    In the book it's called ``M = 8``. It can represent "129 levels of gray".
    Its dimensions are 16x16, but as a diagonal matrix it is 17x17. It is called
    "Diagonal" because the resulting dot pattern is at a 45 degree angle.
    """

    Horizontal3x5: OrderedDitherMatrix = dither.Horizontal3x5()
    """
    Horizontal 3x5

    Horizontal 3x5 is a custom rotated version of Vertical 5x3.
    """

    Vertical5x3: OrderedDitherMatrix = dither.Vertical5x3()
    """
    Vertical 5x3

    Comes from http://caca.zoy.org/study/part2.html
    They say it "creates artistic vertical line artifacts".
    """

    ClusteredDotSpiral5x5: OrderedDitherMatrix = dither.ClusteredDotSpiral5x5()
    """
    Clustered-Dot Spiral 5x5

    Clustered-Dot Spiral 5x5 comes from Figure 5.13 of the book "Digital Halftoning" by
    Robert Ulichney. It can represent "26 levels of gray". Its dimensions are 5x5.

    Instead of alternating dark and light dots like the other clustered-dot
    matrices, the dark parts grow to fill the area.
    """

    ClusteredDotHorizontalLine: OrderedDitherMatrix = dither.ClusteredDotHorizontalLine()
    """
    Clustered-Dot Horizontal Line

    Clustered-Dot Horizontal Line comes from Figure 5.13 of the book "Digital Halftoning" by
    Robert Ulichney. It can represent "37 levels of gray". Its dimensions are 6x6.

    It "clusters pixels about horizontal lines".
    """

    ClusteredDotVerticalLine: OrderedDitherMatrix = dither.ClusteredDotVerticalLine()
    """
    Clustered-Dot Vertical Line

    Clustered-Dot Vertical Line is a custom rotated version of Clustered-Dot Horizontal Line.
    """

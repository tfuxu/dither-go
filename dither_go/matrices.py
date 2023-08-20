# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

from dataclasses import dataclass

from dither_go.bindings import dither


# TODO: Add docstrings to variables (you can do this by putting docstring under the var declaration)

@dataclass(frozen=True)
class ErrorDiffusers:
    """
    Error diffusion matrices
    """

    Simple2D = dither.Simple2D()

    FloydSteinberg = dither.FloydSteinberg()
    FalseFloydSteinberg = dither.FalseFloydSteinberg()

    Stucki = dither.Stucki()
    Burkes = dither.Burkes()
    Atkinson = dither.Atkinson()
    JarvisJudiceNinke = dither.JarvisJudiceNinke()

    Sierra = dither.Sierra()
    Sierra2 = dither.Sierra2()
    Sierra2_4A = dither.Sierra2_4A()
    Sierra3 = dither.Sierra3()
    SierraLite = dither.SierraLite()
    TwoRowSierra = dither.TwoRowSierra()

    StevenPigeon = dither.StevenPigeon()


@dataclass(frozen=True)
class OrderedDitherers:
    """
    Ordered dither matrices
    """

    ClusteredDot4x4 = dither.ClusteredDot4x4()
    ClusteredDot6x6 = dither.ClusteredDot6x6()
    ClusteredDot6x6_2 = dither.ClusteredDot6x6_2()
    ClusteredDot6x6_3 = dither.ClusteredDot6x6_3()
    ClusteredDot8x8 = dither.ClusteredDot8x8()

    ClusteredDotDiagonal6x6 = dither.ClusteredDotDiagonal6x6()
    ClusteredDotDiagonal8x8 = dither.ClusteredDotDiagonal8x8()
    ClusteredDotDiagonal8x8_2 = dither.ClusteredDotDiagonal8x8_2()
    ClusteredDotDiagonal8x8_3 = dither.ClusteredDotDiagonal8x8_3()
    ClusteredDotDiagonal16x16 = dither.ClusteredDotDiagonal16x16()

    Horizontal3x5 = dither.Horizontal3x5()
    Vertical5x3 = dither.Vertical5x3()

    ClusteredDotSpiral5x5 = dither.ClusteredDotSpiral5x5()

    ClusteredDotHorizontalLine = dither.ClusteredDotHorizontalLine()
    ClusteredDotVerticalLine = dither.ClusteredDotVerticalLine()

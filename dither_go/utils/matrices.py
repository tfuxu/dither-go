# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

from dataclasses import asdict
from typing import List, Tuple

from simple_parsing.docstring import get_attribute_docstring

from dither_go import ErrorDiffusionMatrix, OrderedDitherMatrix
from dither_go.matrices import ErrorDiffusers, OrderedDitherers


class MatrixUtils:  # pylint: disable=R0903
    """
    A class for error diffusion and ordered dithering matrices utility methods.
    """

    def __init__(self):
        pass

    def generate_matrices_list(self) -> Tuple[List[Tuple[str, ErrorDiffusionMatrix]], List[Tuple[str, OrderedDitherMatrix]]]:
        """
        Generates a list of available matrices in library with human-readable names.

        :returns: Two lists consisting of error diffusion and ordered dithering matrices with their display names.
        :rtype: Tuple[List[Tuple[str, ErrorDiffusionMatrix]], List[Tuple[str, OrderedDitherMatrix]]]
        """

        error_diffusers = asdict(ErrorDiffusers())
        ordered_ditherers = asdict(OrderedDitherers())

        error_matrices = []
        for key in error_diffusers:
            field_docstring = get_attribute_docstring(ErrorDiffusers, key).docstring_below
            display_name = field_docstring.strip().partition("\n")[0]

            error_matrices.append((display_name, error_diffusers[key]))

        ordered_matrices = []
        for key in ordered_ditherers:
            field_docstring = get_attribute_docstring(OrderedDitherers, key).docstring_below
            display_name = field_docstring.strip().partition("\n")[0]

            ordered_matrices.append((display_name, ordered_ditherers[key]))

        return error_matrices, ordered_matrices

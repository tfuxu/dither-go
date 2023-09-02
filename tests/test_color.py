# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

from dither_go.utils.color import ColorUtils


def test_is_valid_hex():
    """
    Tests if `is_valid_hex()` helper method can properly parse hexadecimal codes
    and translate them to correct RGBA color channels.
    """

    color_utils = ColorUtils()

    test_hex_codes = ["#fff", "#128", "#abdfbe", "#deadbeef"]
    valid_results = [[15, 15, 15], [1, 2, 8], [171, 223, 190], [222, 173, 190, 239]]

    for value, result in zip(test_hex_codes, valid_results):
        assert color_utils.is_valid_hex(value) == result

def test_is_valid_rgba():
    """
    Tests if `is_valid_rgba()` helper method can properly parse RGBA color channel lists.
    """

    color_utils = ColorUtils()

    test_rgba_lists = [[0, 0, 0, 32], [132, 247, 89], [44, 114, 148], [255, 255, 255, 255]]
    valid_results = test_rgba_lists[:]

    for value, result in zip(test_rgba_lists, valid_results):
        assert color_utils.is_valid_rgba(value) == result

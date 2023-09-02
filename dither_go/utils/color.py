# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import List, Union

from dither_go.bindings import dither_go
from dither_go.exceptions import InvalidColorError


class ColorUtils:
    """
    A class for internal color parsing/manipulation utility methods.
    """

    def __init__(self):
        pass

    def color_to_rgba(self, color_value: Union[List[int], str]):
        """
        Converts either an list of RGB color channels or hexadecimal representation
        to the `color.RGBA` Golang object.

        :param color_value: Either an list of RGB color channels or hex color code.
        :type color_value: Union[List[int], str]

        :raises InvalidColorError: When there is an error during color code parsing or
        reading a color representation type.

        :returns: An `color.RGBA` Golang object for use in color palettes.
        """

        if not isinstance(color_value, list) and not isinstance(color_value, str):
            raise InvalidColorError("Invalid format of color value provided")

        if isinstance(color_value, list):
            rgba_list = self.is_valid_rgba(color_value)
        elif isinstance(color_value, str):
            rgba_list = self.is_valid_hex(color_value)

        if len(rgba_list) == 3:
            rgba_list.append(255)

        r, g, b, a = rgba_list

        return dither_go.CreateRGBA(r, g, b, a)

    def is_valid_hex(self, hex_value: str) -> List[int]:
        """
        Checks if provided hexadecimal value is a valid representation
        of a hexadecimal color code and returns an list of RGB color channels
        upon success.

        It supports short hex codes (eg. #fff), normal sized codes and
        extended form with alpha channel (transparency).

        :param hex_value: A hexadecimal value with `#` prefix.
        :type hex_value: :class:`str`

        :raises InvalidColorError: When there is an error during color code parsing.

        :returns: An list of RGB color channels converted from hexadecimal value.
        :rtype: List[int]
        """

        if not hex_value.startswith("#"):
            raise InvalidColorError("Color code isn't prefixed with hash (#) character")

        hex_value = hex_value.lstrip("#")

        if len(hex_value) not in [3, 6, 8]:
            raise InvalidColorError(f"Provided hexadecimal code has an invalid length: {len(hex_value)}")

        index_tuple = (0, 2, 4)
        channel_length = 2

        if len(hex_value) == 8:
            index_tuple = index_tuple + (6,)

        if len(hex_value) == 3:
            index_tuple = (0, 1, 2)
            channel_length = 1

        rgba_list = []
        for i in index_tuple:
            try:
                rgba_list.append(int(hex_value[i:i+channel_length], 16))
            except ValueError as exc:
                raise InvalidColorError("Color channel value in color code isn't an valid hexadecimal number") from exc

        return rgba_list

    def is_valid_rgba(self, rgba_list: List[int]) -> List[int]:
        """
        Checks if provided list of color channel values represents
        a valid RGB-formatted color.

        It supports RGB values with and without the forth alpha channel provided
        (transparency).

        :param rgba_list: A list of RGB color channels.
        :type rgba_list: List[int]

        :raises InvalidColorError: When there is an error during color channel parsing.

        :returns: The provided list as an indication of success.
        :rtype: List[int]
        """

        if len(rgba_list) not in [3, 4]:
            raise InvalidColorError(f"Provided color channel list contains invalid amount of values: {len(rgba_list)}")

        for channel in rgba_list:
            if not isinstance(channel, int):
                try:
                    channel = int(channel)
                except ValueError as exc:
                    raise InvalidColorError("An color channel in provided list is an instance of the unsupported data type") from exc

            if channel not in range(0, 256):
                raise InvalidColorError("Color channel value is outside the (0, 255) range")

        return rgba_list

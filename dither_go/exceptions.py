# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

class DitherGoError(Exception):
    """ Base exception class used by modules in Dither Go. """


class InvalidColorError(DitherGoError):
    """ Raised when there is an error during parsing/converting a color value. """

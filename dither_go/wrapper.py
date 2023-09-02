# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import List, Union

from dither_go.utils.color import ColorUtils
from dither_go.bindings import dither, dither_go


# ---- Classes ---
class Ditherer(dither.Ditherer):
    """
    Ditherer dithers images according to the settings in the class.
    It can be safely reused for many images, and used concurrently.

    Some members of the class are public. Those members can be changed
    in-between dithering images, if you would like to dither again.
    If you change those public methods while an image is being dithered, the
    output image will have problems, so only change in-between dithering.

    You can only set one of Matrix, Mapper, or Special. Trying to dither when
    none or more than one of those are set will cause the function to panic.

    All methods can handle images with transparency, unless otherwise specified.
    Read the docs before using!
    """


class OrderedDitherMatrix(dither.OrderedDitherMatrix):
    """
    OrderedDitherMatrix is used to hold a matrix used for ordered dithering.
    This is useful if you find a matrix somewhere and would like to try it out.
    You can create this class and then give it to PixelMapperFromMatrix.

    The matrix must be rectangular - each slice inside the first one must be the
    same length.

    Max is the value all the matrix values will be divided by. Usually this is the
    product of the dimensions of the matrix (x*y), or the greatest value in the matrix
    plus one. For diagonal matrices or other matrices with repeated values, it is the
    latter.

    Leaving Max as 0 will cause a panic.

    Matrix values should almost always range from 0 to Max-1. If the matrix you found
    ranges from 1 to Max, just subtract 1 from every value when programming it.
    """


# ---- Slices ---
class ErrorDiffusionMatrix(dither.ErrorDiffusionMatrix):
    """
    ErrorDiffusionMatrix holds the matrix for the error-diffusion type of dithering.
    An example of this would be Floyd-Steinberg or Atkinson.

    Zero values can be used to represent pixels that have already been processed.
    The current pixel is assumed to be the right-most zero value in the top row.
    """


# ---- Constructors ---
def new_ditherer(palette):
    """
    Creates a new ``Ditherer`` object that uses a copy of the provided palette.
    If the palette is None, then None will be returned.

    .. note:: All palette colors should be opaque.

    :param palette: A color palette created using ``create_palette`` function.

    :returns: A new ``Ditherer`` Golang object with provided color palette.
    """

    # TODO: Use inherited Dither class instead
    return dither.NewDitherer(palette)


# ---- Library Functions ---
def round_clamp(number: float) -> int:
    """
    Clamps the number and rounds it, rounding ties to the nearest even number.
    This should be used if you're writing your own PixelMapper.

    :param number: An floating-point number.
    :type number: :class:`float`

    :rtype: :class:`int`
    """

    return dither.RoundClamp(number)

def error_diffusion_strength(edm, strength: float):
    """
    Modifies an existing error diffusion matrix so that it will be applied with
    the specified strength.

    ``edm`` is an existing error diffusion matrix class.

    ``strength`` is usually a value from 0 to 1.0, where 1.0 means 100% strength,
    and will not modify the matrix at all.
    It is inversely proportional to contrast - reducing the strength increases
    the contrast. It can be useful at values like 0.8 for reducing noise
    in the dithered image.

    See the documentation for Bayer for more details.
    """

    return dither.ErrorDiffusionStrength(edm, strength)


# ---- Helper Functions ---
def open_image(path: str):
    """
    Opens image file and decodes its contents using ``image.Decode`` Golang function.

    .. note:: Check ``format_matrix.md`` document for information about
    supported image formats.

    :param path: An path to the location of the image.
    :type path: :class:`str`

    :raises Exception: If there is a failure in I/O operations or image decoding.

    :returns: An ``image.Image`` Golang object containing image data.
    """

    try:
        img_data = dither_go.OpenImage(path)
    except Exception as exc:
        raise exc
    else:
        return img_data

def save_image(img_data, output_path: str, encode_format: str) -> None:
    """
    Saves provided image data in specified output path and
    encodes it to the supported format.

    .. note:: Check ``format_matrix.md`` document for information about
    supported image formats and their names used in ``encode_format``.

    :param output_path: An path to the output location of the image.
    :type output_path: :class:`str`

    :param encode_format: A name of the image format used in encoding.
    :type encode_format: :class:`str`

    :raises Exception: If there is a failure in I/O operations or image encoding.

    :rtype: :class:`None`
    """

    try:
        dither_go.SaveImage(img_data, output_path, encode_format)
    except Exception as exc:
        raise exc

def create_palette(color_list: List[Union[str, List[int]]]):
    """
    Creates a new color palette for use in dithered images.

    It supports mixing hexadecimal color codes (in short, normal and extended forms),
    with lists of RGB color channels (with and without alpha channel provided).

    :param color_list: A list with hex color values and/or lists of RGBA channel
    value representations written using integers.
    :type color_list: List[Union[str, List[int]]]

    :raises InvalidColorError: When there is an error during color parsing/conversion.

    :returns: An list of ``color.RGBA`` Golang objects for use in image dithering.
    """

    color_utils = ColorUtils()

    palette = []
    for value in color_list:
        palette.append(color_utils.color_to_rgba(value))

    return dither_go.CreatePalette(*palette)

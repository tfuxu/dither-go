<img src="https://raw.githubusercontent.com/tfuxu/dither-go/master/data/images/david_dithered.png" align="left" height="96px" vspace="10px">

# Dither Go!

Dither Go! is a fast image processing library, making use of `dither` Golang library to provide the most correct image dithering.

> **Warning**
> Keep in mind, that this library is currently in alpha state, and although there probably won't be that many breaking changes (unless there will be in `dither`), there might be some bugs laying around in the less tested parts of the library. If you find some, please report them to the [bug tracker](https://github.com/tfuxu/dither-go/issues).

## Features:

- A vast variety of dithering algorithms built-in with an option to specify your own (under construction),
- Very fast backend written in Go,
- Unique correctness from most dithering libraries, thanks to image linearization and color comparisons based on channel weighting technique,
- Support for images with transparency.

## Types of dithering supported

- Random noise (in grayscale and RGB)
- **Ordered Dithering**
  - Bayer matrix of any size (as long as dimensions are powers of two)
  - Clustered-dot - many different preprogrammed matrices
  - Some unusual horizontal or vertical line matrices
  - Yours?
    - Using `SetOrdered`, this library can dither using any matrix (under construction)
- **Error diffusion dithering**
  - Simple 2D
  - Floyd-Steinberg, False Floyd-Steinberg
  - Jarvis-Judice-Ninke
  - Atkinson
  - Stucki
  - Burkes
  - Sierra/Sierra3, Sierra2, Sierra2-4A/Sierra-Lite
  - [Steven Pigeon](https://hbfs.wordpress.com/2013/12/31/dithering/)

## How to install?

To install Dither Go! from PyPI, setup `venv` and run:
```shell
$ pip install dither-go
```

And import library using `import dither_go`.

## Usage

Here's a simple example using Floyd-Steinberg dithering:
```python
try:
    img = dither_go.open_image("input.jpg")
except Exception as e:
    print(f"Couldn't load the requested image. Exception: {e}")

# This is the color palette used in output image
palette = dither_go.create_palette([
    [0, 0, 0],
    [255, 255, 255],
    # You can put here any color you want
])

# Create new `Ditherer` object using a constructor
ditherer = dither_go.new_ditherer(palette)
ditherer.Matrix = dither_go.ErrorDiffusers.FloydSteinberg

# Dither the image, attempting to modify the existing image
# If it can't then a dithered copy will be returned.
img = ditherer.Dither(img)

dither_go.save_image(img, "dither_go.png", "png")
```
If you always want to dither a copy of the image, you can use `DitherCopy` instead.

Here's how you create a `Ditherer` that does Bayer dithering. Note that `ditherer.SetBayer` is used instead of `ditherer.Matrix`.

```python
ditherer = dither_go.new_ditherer(palette)
ditherer.SetBayer(8, 8, 1.0)  # 8x8 Bayer matrix at 100% strength
```

Here's how you create a `Ditherer` that does clustered-dot dithering - dithering with a predefined matrix.

```python
ditherer = dither_go.new_ditherer(palette)
ditherer.SetOrdered(dither_go.OrderedDitherers.ClusteredDotDiagonal8x8, 1.0)
```

## What method should I use?

Generally, using Floyd-Steinberg serpentine dithering will produce the best results. The code would be:

```python
ditherer = dither_go.new_ditherer(palette)
ditherer.Matrix = dither_go.ErrorDiffusers.FloydSteinberg
ditherer.Serpentine = True
```

Playing with the strength of the matrix might also be useful. The example above is at full strength, but sometimes that's too noisy. The code for 80% strength looks like this:

```python
ditherer.Matrix = dither_go.error_diffusion_strength(dither_go.ErrorDiffusers.FloydSteinberg, 0.8)
```

The main reason for using any other dithering algorithm would be

- **Aesthetics** - dithering can be a cool image effect, and different methods will look different
- **Speed** - error diffusion dithering is sequential and therefore single-threaded. But ordered dithering, like using `Bayer`, will use all available CPUs, which is much faster.

## How to access built-in matrices?

Built-in error diffusion and ordered dither matrices are located in `ErrorDiffusers` and `OrderedDitherers` data classes.

In order to apply error diffusion matrix to `Ditherer`, first construct a new instance by using `new_ditherer()` constructor and set `Matrix` variable value to any of the `ErrorDiffusers` matrices.

To apply ordered dither matrix, use `SetOrdered` method instead.

> **Warning**
> You can't have both types of dither applied at the same time, so in order to change dithering type, you'll need to clear currently used dither type.
>
> To clear error diffusion matrix, set `None` as a value in `Matrix` and to clear ordered dither matrix, use `ClearMapper`.

## How do I get the palette?

Sometimes the palette isn't an option, as it might determined by the hardware. Many e-ink screens can only display black and white for example, and so your palette is chosen for you.

But in most cases you have all the colors available, and so you have to pick the ones that represent your image best. This is called [color quantization](https://en.wikipedia.org/wiki/Color_quantization).

There isn't currently any built-in color quantization functionality available in this library. You'll instead need to use a library for that, like [color-thief](https://github.com/fengsp/color-thief-py) which is the most popular, or something like [colorgram.py](https://github.com/obskyr/colorgram.py) or [Pylette](https://github.com/qTipTip/Pylette). There is also [pywal](https://github.com/dylanaraps/pywal) which you can [use as a module](https://github.com/dylanaraps/pywal/wiki/Using-%60pywal%60-as-a-module).

## Scaling images

A dithered output image will only look right at 100% size. As you scale *down*, the image will immediately get darker, and strange grid-like artifacts will appear, known as a [moiré pattern](https://en.wikipedia.org/wiki/Moir%C3%A9_pattern). This is due to how dithered images work, and is not something this library can fix.

The best thing to do is to scale the *input* image to the *exact* size you want before using this library. But sometimes you want to scale the image up after dithering, to make the dithering effect more obvious for aesthetic purposes.

So for scaling the dithered output image *up* (above 100%), that will only look fine if you use **nearest-neighbor scaling** - the kind of scaling that produces pixelated results. Otherwise the dither pixel values will be blurred and averaged, which will mess things up. And even once you're using that, it will still produce moiré patterns, unless you're scaling by a multiple of the original dimensions. **So when scaling up, you should be scaling by 2x or 3x, rather than a non-integer like 1.34x.**

## Encoding and decoding

Due to how Golang's `image` library works, there is only support for the most basic image formats built-in into the standard library. 

To add more, you need to use custom decoders/encoders, of which Dither Go! already has several added and a couple planned to be added. You can check the [image format matrix](https://github.com/tfuxu/dither-go/blob/master/format_matrix.md) to see which are available and planned to be added.

If you want support for a format which isn't currently on that list, submit a feature request in the [bug tracker](https://github.com/tfuxu/dither-go/issues).

## Tips:

- If the palette is grayscale, the input image should be converted to grayscale first to get accurate results.
- All the `[][]uint` matrices are supposed to be applied with `PixelMapperFromMatrix`.
- You can generate a list of available dither matrices with their display names using `MatrixUtils().generate_matrices_list()` method.

## Notes:

- This README has some of its parts copied from [`dither`](https://github.com/makew0rld/dither) project to provide sufficient information about features of this library

## License

This repository is licensed under the terms of the GNU GPLv3 license. You can find a copy of the license in the COPYING file.

The `dither` library which this project is making use of, is the terms of Mozilla Public License 2.0. The copy of the license can be found [here](https://github.com/makew0rld/dither/blob/master/LICENSE).

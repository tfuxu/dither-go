# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

import dither_go

try:
    img = dither_go.open_image("tests/input.jpg")
except Exception as e:
    raise e

palette = dither_go.create_palette([
    [0, 0, 0, 255],
    [255, 255, 255, 255],
])

dither_object = dither_go.new_ditherer(palette)
dither_object.SetOrdered(dither_go.OrderedDitherers.ClusteredDot4x4, 1.0)

dither_object.Serpentine = False

img = dither_object.Dither(img)

dither_go.save_image(img, "tests/dither_go.png", "png")

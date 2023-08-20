// Copyright 2023, tfuxu <https://github.com/tfuxu>
// SPDX-License-Identifier: GPL-3.0-or-later

package dither_go

import (
	"os"
	"errors"
)

import (
	"image"
	"image/gif"
	"image/png"
	"image/jpeg"
	"image/color"
	"golang.org/x/image/bmp"
	"golang.org/x/image/tiff"
	_ "golang.org/x/image/webp"
	"github.com/kolesa-team/go-webp/webp"
)

// OpenImage opens image file and decodes its contents
// using image.Decode function.
func OpenImage(path string) (image.Image, error) {
	reader, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer reader.Close()

	img, _, err := image.Decode(reader)
	if err != nil {
		return nil, err
	}

	return img, nil
}

// SaveImage saves provided image data in specified output path and
// encodes it to the supported format.
func SaveImage(img_data image.Image, output_path string, encode_format string) error {
	writer, err := os.Create(output_path)
	if err != nil {
		return err
	}

	var encode_err error

	// TODO: Inmplement customization of output quality, lossless mode and other format-specific options in future
	switch encode_format {
	case "png":
		encode_err = png.Encode(writer, img_data)
	case "jpeg":
		encode_err = jpeg.Encode(writer, img_data, nil)
	case "bmp":
		encode_err = bmp.Encode(writer, img_data)
	case "gif":
		encode_err = gif.Encode(writer, img_data, nil)
	case "jxl":
		encode_err = errors.New("JXL format is currently unsupported")
	case "webp":
		encode_err = webp.Encode(writer, img_data, nil)
	case "tiff":
		encode_err = tiff.Encode(writer, img_data, nil)
	case "heif":
		// TODO: Implement in future: github.com/strukturag/libheif/go/heif
		encode_err = errors.New("HEIF format is currently unsupported")
	case "avif":
		// TODO: Implement in future: github.com/strukturag/libheif/go/heif
		encode_err = errors.New("AVIF format is currently unsupported")
	default:
		encode_err = errors.New("unknown format name provided")
	}

	if encode_err != nil {
		writer.Close()
		return encode_err
	}

	if err := writer.Close(); err != nil {
		return err
	}

	return nil
}

// CreateRGBA creates new color.RGBA structure with
// provided (r,g,b,a) color channels.
//
// NOTE: Argument types are set to unint8, values higher than 255 will result
// in 'Out of range' errors.
func CreateRGBA(r uint8, g uint8, b uint8, a uint8) color.RGBA {
	return color.RGBA{r, g, b, a}
}

// CreatePalette creates a palette slice of variable amount
// of color.RGBA structures.
//
// WARNING: Always create color.RGBA values with CreateRGBA() function
// to avoid accessing invalid memory addresses.
func CreatePalette(colors ...color.Color) []color.Color {
	var palette []color.Color
	palette = append(palette, colors...)

	return palette
}

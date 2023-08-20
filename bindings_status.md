## Supported features:
- [x] RoundClamp
- [x] Ditherer:
    - [x] `NewDitherer`
    - [x] `Dither`
    - [ ] `DitherConfig`
    - [x] `DitherCopy`
    - [ ] `DitherCopyConfig`
    - [x] `DitherPaletted`
    - [ ] `DitherPalettedConfig`
    - [x] `Draw`
    - [x] `GetColorModel`
    - [x] `GetPalette`
    - [x] `Quantize`
- [x] ErrorDiffusionMatrix:
    - [x] `CurrentPixel`
    - [ ] `Offset`
- [x] ErrorDiffusionStrength
- [x] OrderedDitherMatrix
- [ ] PixelMapper (currently privated):
    - [ ] `Bayer` (use `Ditherer.SetBayer` instead)
    - [ ] `PixelMapperFromMatrix` (use `Ditherer.SetOrdered` instead)
    - [ ] `RandomNoiseGrayscale` (use `Ditherer.SetRandomGrayscale` instead)
    - [ ] `RandomNoiseRGB` (use `Ditherer.SetRandomRGB` instead)

## Notes:
Check https://github.com/go-python/gopy/pull/282 to see why some methods are currently unsupported.

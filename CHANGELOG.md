# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2023-12-26

### Changed

- updated to `dither` v2.4.0
- updated to `gopy` v0.4.8
- updated to `image` v0.14.0

### Fixed

- `simple_parsing` not being in project configuration dependencies

## [0.3.0] - 2023-09-09

### Added

- `MatrixUtils` helper class with `generate_matrices_list()` method
- Docstrings for `ErrorDiffusers` and `OrderedDitherers` dataclass fields

## [0.2.1] - 2023-09-04

Nothing has changed, this is just a PyPI release.

## [0.2.0] - 2023-09-04

### Added

- New `test_color` unit test

### Changed

- From now accept RGBA color channel lists and hex color codes as a input parameter to `create_palette` wrapper function

### Removed

- `RGBA` wrapper function, as `create_palette` automatically converts input to `color.RGBA` Golang objects

## [0.1.0] - 2023-08-20

Initial release.

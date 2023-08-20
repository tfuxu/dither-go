# Dither Go!

Dither Go! is a Python package providing bindings for [`dither`](https://github.com/makew0rld/dither) Golang library.

> [!NOTE]
> README is currently under construction. More sections comming soon!

## How to access built-in matrices?
Built-in error diffusion and ordered dither matrices are located in `ErrorDiffusers` and `OrderedDitherers` data classes.

In order to apply error diffusion matrix to `Ditherer`, first construct a new instance by using `new_ditherer()` constructor and set `Matrix` variable value to any of `ErrorDiffusers` matrices.

To apply ordered dither matrix, use `SetOrdered` method instead.

## How to update bindings:

#### Prerequisites:

The following packages are required to properly compile bindings:

- Go (>= 1.15.0) `go`
- Python 3 `python`

#### Build instructions:

(Optional) Setup venv:
```sh
python -m venv venv
```

Install Goimports, Gopy and Python requirements:

```sh
go install golang.org/x/tools/cmd/goimports@latest
go install github.com/go-python/gopy@latest
pip install -r requirements.txt
```

Compile bindings using `gopy build`:

```sh
gopy build -no-make -output=dither_go/bindings -vm=python3 ./dither_go github.com/tfuxu/dither-gopy
```

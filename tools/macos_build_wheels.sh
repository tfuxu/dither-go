#!/bin/bash

set -e

START_GROUP=0

trap _end_group EXIT

_end_group() (
    if [ "$START_GROUP" == "1" ]
    then
        echo "::endgroup::"
        START_GROUP=0
    fi
)

_start_group() (
    _end_group
    echo "::group::$1"
    START_GROUP=1
)

install_python() (
    PY_MINOR=$1
    brew install python@3.$PY_MINOR
)

build_wheel() (
    PY_MINOR=$1
    ln -sf /usr/local/opt/python@3.$PY_MINOR/bin/python3.$PY_MINOR  /usr/local/bin/python_for_build
    /usr/local/bin/python_for_build --version
    /usr/local/bin/python_for_build -m pip install cibuildwheel==2.15.0 pybindgen
    CIBW_BUILD="cp3$PY_MINOR-*" /usr/local/bin/python_for_build -m cibuildwheel --output-dir wheelhouse .
)

test_wheel() (
    PY_MINOR=$1
    if [ "$CIBW_ARCHS" == "x86_64" ]
    then
        ln -sf /usr/local/opt/python@3.$PY_MINOR/bin/python3.$PY_MINOR  /usr/local/bin/python_for_build
        /usr/local/bin/python_for_build -m pip install wheelhouse/*cp3$PY_MINOR*.whl
        /usr/local/bin/python_for_build -c "import dither_go; print(dither_go)"
    fi
)

_start_group "Python 3.8"
install_python 8
build_wheel 8
test_wheel 8

_start_group "Python 3.9"
install_python 9
build_wheel 9
test_wheel 9

_start_group "Python 3.10"
install_python 10
build_wheel 10
test_wheel 10

_start_group "Python 3.11"
install_python 11
build_wheel 11
test_wheel 11

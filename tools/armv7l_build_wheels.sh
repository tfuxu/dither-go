#!/bin/bash

PYTHON3_VERSION=$1

set -e

build_wheel() (
    PY_VER=$1
    mkdir build$PY_VER
    cd build$PY_VER
    pip$PY_VER install build
    python$PY_VER -m build ..
)

test_wheel() (
    PY_VER=$1
    cd build$PY_VER
    pip$PY_VER install *armv7l.whl
    python$PY_VER -c "import dither_go; print(dither_go)"
)

repair_wheel() (
    PY_VER=$1
    cd build$PY_VER
    auditwheel repair *armv7l.whl
)

build_wheel 3.$PYTHON3_VERSION
repair_wheel 3.$PYTHON3_VERSION
test_wheel 3.$PYTHON3_VERSION

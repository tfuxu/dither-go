#!/bin/bash

set -e

compile_libwebp() (
    curl -o libwebp.tar.gz https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-1.3.1.tar.gz
    tar -xzf libwebp.tar.gz
    cd libwebp-1.3.1
    ./configure
    make
    make install
)

compile_libwebp

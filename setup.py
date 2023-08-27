# Copyright 2023, popatam, bjia56, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import shutil
import subprocess
import sys

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

if sys.platform == 'darwin':
    # PYTHON_BINARY_PATH is setting explicitly for 310 and 311, see build_wheel.yml
    # on macos PYTHON_BINARY_PATH must be python bin installed from python.org
    PYTHON_BINARY = os.getenv("PYTHON_BINARY_PATH", sys.executable)
else:
    # windown & linux
    PYTHON_BINARY = sys.executable


def _generate_path_with_gopath() -> str:
    go_path = subprocess.check_output(["go", "env", "GOPATH"]).decode("utf-8").strip()
    path_val = f'{os.getenv("PATH")}:{go_path}/bin'

    return path_val


class CustomBuildExt(build_ext):
    def build_extension(self, ext: Extension):
        bin_path = _generate_path_with_gopath()
        go_env = json.loads(subprocess.check_output(["go", "env", "-json"]).decode("utf-8").strip())

        destination = os.path.dirname(os.path.abspath(self.get_ext_fullpath(ext.name))) + "/dither_go/bindings"
        if os.path.isdir(destination):
            # clean up destination in case it has existing build artifacts
            shutil.rmtree(destination)

        env = {
            "PATH": bin_path,
            **go_env,
            "CGO_LDFLAGS_ALLOW": ".*",
        }

        # https://stackoverflow.com/a/64706392
        if sys.platform == "win32":
            env["SYSTEMROOT"] = os.environ.get("SYSTEMROOT", "")

        if sys.platform == "darwin":
            min_ver = os.environ.get("MACOSX_DEPLOYMENT_TARGET", "")
            env["MACOSX_DEPLOYMENT_TARGET"] = min_ver
            env["CGO_LDFLAGS"] = "-mmacosx-version-min=" + min_ver
            env["CGO_CFLAGS"] = "-mmacosx-version-min=" + min_ver

        subprocess.check_call(
            [
                "gopy",
                "build",
                "-no-make",
                "-dynamic-link=True",
                "-symbols=False",
                "-output",
                destination,
                "-vm",
                PYTHON_BINARY,
                *ext.sources,
            ],
            env=env,
        )


setup(
    cmdclass={
        "build_ext": CustomBuildExt,
    },
    ext_modules=[
        Extension("dither_go", sources=["./dither_go", "github.com/tfuxu/dither-gopy"])
    ],
)

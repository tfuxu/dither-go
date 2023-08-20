# Copyright 2023, popatam, bjia56, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import subprocess
import sys

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


if sys.platform == 'darwin':
    # PYTHON_BINARY_PATH is setting explicitly for 310 and 311, see build_wheel.yml
    # on macos PYTHON_BINARY_PATH must be python bin installed from python.org
    PYTHON_BINARY = os.getenv("PYTHON_BINARY_PATH", sys.executable)
    if PYTHON_BINARY == sys.executable:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pybindgen'])
else:
    # linux & windows
    PYTHON_BINARY = sys.executable
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pybindgen'])


def _generate_path_with_gopath() -> str:
    go_path = subprocess.check_output(["go", "env", "GOPATH"]).decode("utf-8").strip()
    path_val = f'{os.getenv("PATH")}:{go_path}/bin'

    return path_val


class CustomBuildExt(build_ext):
    def build_extension(self, ext: Extension):
        bin_path = _generate_path_with_gopath()
        go_env = json.loads(subprocess.check_output(["go", "env", "-json"]).decode("utf-8").strip())

        destination = os.path.dirname(os.path.abspath(self.get_ext_fullpath(ext.name))) + "/dither_go/bindings"

        env = {
            "PATH": bin_path,
            **go_env,
            "CGO_LDFLAGS_ALLOW": ".*",
        }

        # https://stackoverflow.com/a/64706392
        if sys.platform == "win32":
            env["SYSTEMROOT"] = os.environ.get("SYSTEMROOT", "")

        subprocess.check_call(
            [
                "gopy",
                "build",
                "-no-make",
                "-dynamic-link=True",
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

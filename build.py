from conan.packager import ConanMultiPackager
from conans.tools import os_info
import copy

if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing",
                                 reference="7z-installer/16.02")
    builder.add()
    builder.run()

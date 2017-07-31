from conans import ConanFile, CMake
import os


class MinGWInstallerTestConan(ConanFile):
    settings = None

    def test(self):
        self.run("7z --help")

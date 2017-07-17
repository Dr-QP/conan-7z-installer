from conans import ConanFile, tools
import os


class SevenZinstallerConan(ConanFile):
    name = "7z-installer"
    version = "16.02"
    license = "GNU LGPL + unRAR restriction"
    url = "https://github.com/Dr-QP/conan-7z-installer"
    description = "7-Zip is a file archiver for Windows NT / 2000 / 2003 / 2008 / 2012 / XP / Vista / 7 / 8 / 10"
    settings = None
    exports = "sources/*"
    build_policy = "missing"

    def configure(self):
        if not tools.os_info.is_windows:
            raise Exception("7z-installer package is designed for use on Windows host only")

    def package(self):
        self.copy("*", dst="bin", src="sources")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))

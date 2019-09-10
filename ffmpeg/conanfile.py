from conans import ConanFile


class FfmpegConan(ConanFile):
    name = "ffmpeg"
    version = "1.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Ffmpeg here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    build_requires = "fontconfig/1.0", "harfbuzz/1.0"

    def source(self):
        pass

    def build(self):
        self.run("touch libavcodec.so")

    def package(self):
        self.copy("*.so", dst="lib")

    def package_info(self):
        self.cpp_info.libs = ["ffmpeg"]

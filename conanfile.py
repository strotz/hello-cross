from conans import ConanFile, CMake


class HelloConan(ConanFile):
    name = "Hello"
    version = "0.1"
    license = "MIT"
    url = "github.com/strotz/hello-cross"
    description = "cross compile sample"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*", dst="bin", src="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

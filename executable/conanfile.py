
import os.path

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout


class ExecutableRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("spdlog/1.14.0")
        self.requires("gtest/1.15.0")

    def configure(self):
        self.options["*"].shared = False
        pass

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure()  # equivalent to self.run("cmake . <other args>")
        cmake.build() # equivalent to self.run("cmake --build . <other args>")
        if not self.conf.get("tools.build:skip_test", default=False):
            test_folder = os.path.join(self.build_folder, "tests")
            self.run(os.path.join(test_folder, "tests"))
        pass

    def layout(self):
        cmake_layout(self)
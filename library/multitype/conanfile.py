
import os.path

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import copy


class LibraryRecipe(ConanFile):
    name = "m_simple"
    version = "0.1.0"

    # Optional metadata
    author = "Dimitrius-dev"
    url = "https://github.com/m_simple"
    description = "library example"
    topics = ("library", "example")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}


    library_dir = "conan_lib"
    unit_tests_dir = "tests"

    # Sources are located in the same place as this recipe, copy them to the recipe
    def export_sources(self):
        copy(self, "*", os.path.join(self.recipe_folder, self.library_dir), self.export_sources_folder, keep_path = True)
        pass

    def requirements(self):
        self.requires("spdlog/1.14.1")
        self.test_requires("gtest/1.15.0")
        pass

    def configure(self):
        self.options["spdlog"].shared = False
        self.options["gtest"].shared = False
        self.options["*"].fPIC = True
        pass

    def layout(self):
        cmake_layout(self)
        pass

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        if not self.conf.get("tools.build:skip_test", default=False):
            test_folder = os.path.join(self.build_folder, self.unit_tests_dir)
            self.run(os.path.join(test_folder, "tests"))
        pass

    def package(self):
        # set public_headers
        header_dirs = os.listdir(self.source_folder)
        header_dirs.remove(self.unit_tests_dir)
        for lib_dir in header_dirs:
            copy(self, "*",
                 src=os.path.join(self.source_folder, lib_dir, "include"),
                 dst=os.path.join(self.package_folder, "include", lib_dir)
                 )

        cmake = CMake(self)
        cmake.install()
        pass

    def package_info(self):
        self.cpp_info.libs = [self.name]
        self.cpp_info.set_property("cmake_file_name", self.name)
        self.cpp_info.set_property("cmake_target_name", f'{self.name}::{self.name}')


        self.cpp_info.components["part1_lib"].libs = ["part1"]
        self.cpp_info.components["part1_lib"].set_property("cmake_target_name", f'{self.name}::part1')
        self.cpp_info.components["part1_lib"].includedirs = ["include/part1"]
        self.cpp_info.components["part1_lib"].requires = ["spdlog::spdlog"]

        self.cpp_info.components["part2_lib"].libs = ["part2"]
        self.cpp_info.components["part2_lib"].set_property("cmake_target_name", f'{self.name}::part2')
        self.cpp_info.components["part2_lib"].includedirs = ["include/part2"]

        self.cpp_info.components["ho_part2_lib"].includedirs = ["include/ho_part2"]
        pass
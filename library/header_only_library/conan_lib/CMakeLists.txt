cmake_minimum_required(VERSION 3.26)
project(ho_simple)


add_subdirectory(ho_simple)

if (NOT BUILD_TESTING STREQUAL OFF)
    add_subdirectory(tests)
endif()


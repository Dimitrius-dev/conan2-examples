cmake_minimum_required(VERSION 3.26)
project(simple)


add_subdirectory(simple)

if (NOT BUILD_TESTING STREQUAL OFF)
    add_subdirectory(tests)
endif()


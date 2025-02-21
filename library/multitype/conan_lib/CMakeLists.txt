cmake_minimum_required(VERSION 3.26)
project(simple)


add_subdirectory(part1)
add_subdirectory(part2)
add_subdirectory(ho_part2)

if (NOT BUILD_TESTING STREQUAL OFF)
    add_subdirectory(tests)
endif()


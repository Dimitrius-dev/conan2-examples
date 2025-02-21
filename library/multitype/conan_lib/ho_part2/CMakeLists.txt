cmake_minimum_required(VERSION 3.26)


add_library(ho_part2 INTERFACE)

target_include_directories(ho_part2 INTERFACE include)

install(TARGETS ho_part2)

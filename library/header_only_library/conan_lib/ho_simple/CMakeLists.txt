cmake_minimum_required(VERSION 3.26)


add_library(ho_simple INTERFACE)

target_include_directories(ho_simple INTERFACE include)

install(TARGETS simple)

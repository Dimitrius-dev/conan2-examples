cmake_minimum_required(VERSION 3.15)
project(test_package)


find_package(ho_simple REQUIRED)

add_executable(test_package
        src/test_package.cpp
)

target_link_libraries(test_package
        ho_simple::ho_simple
)

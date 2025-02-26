cmake_minimum_required(VERSION 3.26)


add_executable(tests
        src/tests/test.cpp
)

target_include_directories(tests PUBLIC include)

find_package(GTest 1.15.0 REQUIRED)

target_link_libraries(tests PUBLIC
        ho_simple
        gtest::gtest
)

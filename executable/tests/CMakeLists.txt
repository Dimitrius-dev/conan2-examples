
cmake_minimum_required(VERSION 3.26)


add_executable(tests
        source/tests.cpp
)

target_include_directories(tests PRIVATE
        include
)

find_package(GTest 1.15.0 REQUIRED)

target_link_libraries(tests PRIVATE
        gtest::gtest
)

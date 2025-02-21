cmake_minimum_required(VERSION 3.26)


add_library(part2
        src/Tool1.cpp
)

target_include_directories(part2 PUBLIC include)

install(TARGETS part2)

cmake_minimum_required(VERSION 3.26)


add_library(part1
        src/Printer.cpp
)

target_include_directories(part1 PUBLIC include)

find_package(spdlog 1.14.1 REQUIRED)

target_link_libraries(part1 PUBLIC
        spdlog::spdlog
)

install(TARGETS part1)

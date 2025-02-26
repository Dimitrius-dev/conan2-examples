cmake_minimum_required(VERSION 3.26)


add_library(main STATIC
        source/Tool.cpp
        source/Substract.cpp
        source/Printer.cpp
)

target_include_directories(main PUBLIC
        include
)

find_package(spdlog 1.14.0 REQUIRED)

target_link_libraries(main PRIVATE
        spdlog::spdlog
)

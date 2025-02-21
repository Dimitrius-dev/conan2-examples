cmake_minimum_required(VERSION 3.26)


add_library(simple
        src/Tool1.cpp
        src/Tool2.cpp
        src/Printer.cpp
)

target_include_directories(simple PUBLIC include)

find_package(spdlog 1.14.1 REQUIRED)

target_link_libraries(simple PUBLIC
        spdlog::spdlog
)

install(TARGETS simple)

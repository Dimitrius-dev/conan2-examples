cmake_minimum_required(VERSION 3.26)


add_executable(exec
        source/main.cpp
)

target_include_directories(exec PRIVATE
        include
)

target_link_libraries(exec PRIVATE
        main
)
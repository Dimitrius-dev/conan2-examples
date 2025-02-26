cmake_minimum_required(VERSION 3.15)
project(test_package)


find_package(m_simple REQUIRED)

add_executable(test_package
        src/test_package.cpp
)

target_link_libraries(test_package
        m_simple::m_simple
)

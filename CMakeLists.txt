cmake_minimum_required(VERSION 3.8)
project(max_clique)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Boost 1.40 REQUIRED COMPONENTS graph random)
include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIR})

add_executable(${PROJECT_NAME} ./src/main.cpp)

target_link_libraries(${PROJECT_NAME} Boost::graph Boost::random)

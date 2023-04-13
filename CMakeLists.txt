cmake_minimum_required(VERSION 3.10)
project(filesystem)

find_package(Python COMPONENTS Interpreter)

# Use waf to resolve dependencies
if(NOT DEFINED STEINWURF_RESOLVE)
    message(STATUS "Resolving dependencies...")
    execute_process(
        COMMAND ${Python_EXECUTABLE} waf resolve ${STEINWURF_RESOLVE_OPTIONS}
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        RESULT_VARIABLE STATUS)

    if(STATUS AND NOT STATUS EQUAL 0)
        message(FATAL_ERROR "Failed: ${STATUS}")
    endif()

    set(STEINWURF_RESOLVE "${CMAKE_CURRENT_SOURCE_DIR}/resolve_symlinks")
    set(STEINWURF_TOP_NAME filesytem)
endif()

# Define library
add_library(filesystem INTERFACE)
target_compile_features(asio INTERFACE cxx_std_14)

target_include_directories(
    asio INTERFACE "${STEINWURF_RESOLVE}/filesystem-source/include")

add_library(steinwurf::filesystem ALIAS filesystem)

# Install headers
install(
    DIRECTORY "${STEINWURF_RESOLVE}/filesystem-source/include"
    DESTINATION ${CMAKE_INSTALL_PREFIX}/include
    FILES_MATCHING
    PATTERN *.hpp)

cmake_minimum_required(VERSION 3.10)
project(test)

set(OpenCV_DIR C:/Users/Michael/Desktop/opencv/build/x64/mingw/lib)	
include_directories(eigen-3.3.9)
find_package(OpenCV REQUIRED)
set(SOURCES VideoStreamReader.cpp)
add_executable(${PROJECT_NAME} ${SOURCES})


target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})

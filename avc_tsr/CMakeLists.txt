cmake_minimum_required(VERSION 2.8.3)
project(avc_tsr)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  message_generation	
)

find_package(OpenCV REQUIRED)


catkin_package(
  LIBRARIES avc_tsr
  CATKIN_DEPENDS roscpp std_msgs
  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
  /usr/local/include/
)

add_executable(avc_tsr src/main.cpp)
## Specify libraries to link a library or executable target against
 target_link_libraries(avc_tsr
   ${catkin_LIBRARIES}
   ${OpenCV_LIBS}
   ${OpenCV_LIBRARIES}
 )


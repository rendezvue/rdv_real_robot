cmake_minimum_required(VERSION 3.0.2)
project(rdv_real_robot)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  urdf
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES rdv_gazebo_master
#  CATKIN_DEPENDS gazebo launch roscpp roslaunch rospy std_msgs urdf
#  DEPENDS system_lib
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

find_package(roslaunch)

# foreach(dir config launch meshes urdf rviz)
foreach(dir launch urdf rviz)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
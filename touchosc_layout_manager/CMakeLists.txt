cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

rosbuild_init()

# Generate py files from ui using pyside-uic
set(UI_CLASS_NAME touchosclayoutmanagerwindow)
execute_process(COMMAND pyside-uic -o ${PROJECT_SOURCE_DIR}/src/${PROJECT_NAME}/${UI_CLASS_NAME}.py ${PROJECT_SOURCE_DIR}/ui/${UI_CLASS_NAME}.ui)

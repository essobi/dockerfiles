# This is an auto generated Dockerfile for ros:desktop-full  
# generated from docker_images/create_ros_image.Dockerfile.em  
FROM osrf/ros:kinetic-desktop-full  
  
# install ros packages  
RUN apt-get update && apt-get install -y \  
ros-kinetic-pr2-common ros-kinetic-rqt-gui ros-kinetic-pr2-dashboard-
aggregator ros-kinetic-rqt \  
libglfw3-dev libglfw3 clang-tidy-5.0 clang-5.0 cmake cmake-curses-gui
libgtest-dev python-software-properties software-properties-common  
RUN cd /usr/src/gtest && cmake CMakeLists.txt && make  
  
# install QT5  
RUN add-apt-repository ppa:beineri/opt-qt-5.10.1-xenial -y  
RUN apt-get update && apt-get install -y qt510base  


FROM osrf/ros:indigo-desktop-full  
  
MAINTAINER Iason Sarantopoulos <iasons@iti.gr>  
  
RUN apt-get update && apt-get install -yy build-essential  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Dependencies for ramcip_grasp_visualization  
RUN apt-get install -yy ros-indigo-rviz-visual-tools  
  
# Dependencies for kuka-server  
RUN apt-get install -yy \  
qt5-default \  
libarmadillo4 \  
libarmadillo-dev  
  
ENV CATKIN_WS=/root/catkin_ws  
  
# Create catkin workspace  
RUN source /opt/ros/indigo/setup.bash && \  
mkdir -p $CATKIN_WS/src && cd $CATKIN_WS/src && catkin_init_workspace && \  
cd $CATKIN_WS && catkin_make && source $CATKIN_WS/devel/setup.bash  
  
# Build the code  
ENTRYPOINT source /opt/ros/indigo/setup.bash && cd $CATKIN_WS && catkin_make
&& catkin_make run_tests  


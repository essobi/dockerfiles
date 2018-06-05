# This file is based on  
#
https://github.com/osrf/docker_images/blob/5399f380af0a7735405a4b6a07c6c40b867563bd/ros/kinetic/ubuntu/xenial/perception/Dockerfile  
FROM ros:kinetic-ros-base-xenial  
  
# install ros packages  
RUN echo "deb http://packages.ros.org/ros-shadow-fixed/ubuntu xenial main" >>
\  
/etc/apt/sources.list.d/ros-latest.list \  
&& apt-get update && apt-get install -y \  
ros-kinetic-perception=1.3.1-0* \  
&& apt -y upgrade ros-kinetic-catkin \  
&& rm -rf /var/lib/apt/lists/*  


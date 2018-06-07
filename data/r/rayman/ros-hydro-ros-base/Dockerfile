FROM ubuntu:12.04  
MAINTAINER Ramon Wijnands <rayman747@hotmail.com>  
  
# Use the "noninteractive" debconf frontend since we're installing in a non-
interactive way.  
ENV DEBIAN_FRONTEND noninteractive  
  
# install the required tools for installing ROS  
RUN apt-get update && apt-get install -y \  
apt-utils  
RUN apt-get install -y \  
wget \  
sudo \  
ca-certificates # below we use https  
  
RUN wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - |
sudo apt-key add -  
RUN sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" >
/etc/apt/sources.list.d/ros-latest.list'  
  
RUN sudo apt-get update && sudo apt-get install -y ros-hydro-ros-base  
  


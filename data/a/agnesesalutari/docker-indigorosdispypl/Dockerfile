# This is an auto generated Dockerfile for ros:desktop-full  
# generated from docker_images/create_ros_image.Dockerfile.em  
FROM osrf/ros:indigo-desktop-trusty  
  
MAINTAINER Agnese Salutari @agnsal  
  
# Install ROS packages  
RUN apt-get update && apt-get install -y \  
ros-indigo-desktop-full=1.1.5-0* \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Python3, Redis and SICStus Prolog dependencies  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y libc6-i386 && apt-get install -y lib32ncurses5 && apt-
get install -y lib32stdc++6 && apt-get install -y vim && apt-get install -y
build-essential && apt-get -y install wget git  
RUN apt-get -y install python python-pip python3-pip redis-server python-redis
git build-essential libevent-dev  
RUN /etc/init.d/redis-server start  
  
# Install SWI Prolog and its dependencies  
RUN apt-get update  
RUN apt-get -y install software-properties-common  
RUN yes "yes" | sudo apt-add-repository ppa:swi-prolog/stable  
RUN apt-get -y install swi-prolog  
  
# ROS configuration  
RUN export ROS_MASTER_URI="http://127.0.0.1:11311" && export
ROS_HOSTNAME="127.0.0.1" && export ROS_IP="127.0.0.1"  
  
# Redis port  
EXPOSE 6379/tcp  


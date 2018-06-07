FROM ubuntu:12.04  
MAINTAINER Ingo Lütkebohle <ingo.luetkebohle@ipvs.uni-stuttgart.de>  
RUN apt-get -y install wget  
RUN echo "deb http://packages.ros.org/ros/ubuntu precise main" >
/etc/apt/sources.list.d/ros-latest.list  
RUN wget http://packages.ros.org/ros.key -O - | apt-key add -  
RUN apt-get update  
RUN apt-get -y install ros-groovy-pr2-desktop ros-groovy-pr2-navigation-apps
python-rosdep python-rosdistro python-rosinstall python-rosinstall-generator
python-rospkg python-wstool python-vcstools python-catkin-pkg libopenni-nite-
dev  
  


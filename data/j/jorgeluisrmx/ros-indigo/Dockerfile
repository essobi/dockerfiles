############################################################  
  
# Dockerfile to build Ubuntu:14.04 \+ ROS-Indigo-desktop-full  
  
# + C/C++, Python dev libs image  
  
############################################################  
  
# From inside this folder  
# docker build -t jorgeluisrmx/ros-indigo  
# From DockerHub  
# docker pull jorgeluisrmx/ros-indigo  
# Basic run  
# docker run -it jorgeluisrmx/ros-indigo /bin/bash  
  
FROM jorgeluisrmx/ubuntu-dev-base  
MAINTAINER jorgeluisrmx "jorgeluisrmx@gmail.com"  
  
# ROS Indigo desktop full installation  
RUN wget http://packages.ros.org/ros.key -O - | apt-key add -  
  
RUN echo "deb http://packages.ros.org/ros/ubuntu trusty main" >
/etc/apt/sources.list.d/ros-latest.list  
  
RUN apt-get update  
  
RUN apt-get install -y ros-indigo-desktop-full  
  
RUN rosdep init  
RUN rosdep update  
RUN echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc  
  
RUN apt-get install -y python-rosinstall  


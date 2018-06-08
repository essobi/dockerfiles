FROM mirsking/ubuntu:14.04  
MAINTAINER Mirs King <mirsking@gmail.com>  
  
# common apps  
RUN apt-get -y update \  
&& apt-get install wget curl openssh-server locate \  
software-properties-common \  
git mercurial -y  
  
RUN sh -c '. /etc/lsb-release && echo "deb
http://mirrors.ustc.edu.cn/ros/ubuntu/ $DISTRIB_CODENAME main" >
/etc/apt/sources.list.d/ros-latest.list'  
  
RUN wget http://packages.ros.org/ros.key -O - | apt-key add - -y  
  
RUN apt-get update && apt-get -y install ros-indigo-desktop-full  
  
RUN echo source /opt/ros/indigo/setup.bash > ~/.bashrc  
  


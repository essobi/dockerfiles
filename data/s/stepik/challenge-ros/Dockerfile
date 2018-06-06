FROM ubuntu:16.04  
MAINTAINER Artyom Filatov <art32fil@gmail.com>  
  
RUN apt-get update \  
&& apt-get -y install openssh-server lsb-release nano \  
&& sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc)
main" > /etc/apt/sources.list.d/ros-latest.list' \  
&& apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key
421C365BD9FF1F717815A3895523BAEEB01FA116 \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd -m box  
  
RUN apt-get update \  
&& apt-get -y install ros-kinetic-ros-base \  
&& rosdep init \  
&& rosdep update \  
&& /bin/bash -c "source /opt/ros/kinetic/setup.bash" \  
&& apt-get -y install python-rosinstall python-rosinstall-generator python-
wstool build-essential \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /.box/bashrc.d/box  
COPY ssh /root/.ssh  
COPY bashrc/box /home/box/.bashrc  
  
COPY greeting /.greeting  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  


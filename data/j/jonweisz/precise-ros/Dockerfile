FROM ubuntu:12.04  
MAINTAINER Jon Weisz <jon.weisz@gmail.com>  
#Builds a base vanilla groovy-precise image  
#  
RUN apt-get -q update  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y apt-utils  
RUN apt-get upgrade -y  
  
ENV DISTRO precise  
ENV ROSDISTRO groovy  
  
# minimum installation  
RUN apt-get install -y software-properties-common ssh sudo wget curl
emacs23-nox lsb-release  
  
#minimal ROS Install  
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $DISTRO main" >
/etc/apt/sources.list.d/ros-latest.list'  
RUN wget http://packages.ros.org/ros.key -O - | apt-key add -  
RUN apt-get update  
RUN apt-get install -y ros-groovy-desktop-full  
  
# add rosuser user  
ENV USERNAME rosuser  
ENV HOME /home/$USERNAME  
RUN mkdir -p $HOME  
RUN useradd $USERNAME  
RUN echo "$USERNAME:$USERNAME" | chpasswd  
RUN echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
RUN chown -R $USERNAME:$USERNAME $HOME  
  
# change user  
USER rosuser  
WORKDIR /home/rosuser/  
  
RUN echo "source $HOME/ros/hydro/devel/setup.bash" >> $HOME/.bashrc  
  
ENTRYPOINT "/bin/bash"  


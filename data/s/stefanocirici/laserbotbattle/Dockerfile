FROM ubuntu:16.04  
LABEL maintainer="Stefano Cirici"  
LABEL maintaineremail="stefanocirici@gmail.com"  
LABEL version="1.0"  
LABEL description="ubuntu 16.04 image for webserver for laser_bot_battle
project"  
LABEL project="laser_bot_battle"  
LABEL projecturl="https://github.com/ludusrusso/pp-robot-2018"  
  
RUN apt-get update && apt-get install -y locales \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN apt-get update && apt-get upgrade -y  
  
# install ROS  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116  
RUN echo "deb http://packages.ros.org/ros/ubuntu xenial main" >
/etc/apt/sources.list.d/ros-latest.list  
RUN apt-get update && apt-get install --no-install-recommends -y \  
python-rosdep \  
python-rosinstall \  
python-vcstools \  
g++  
  
#packages for LaserBot Battle  
RUN apt-get install --no-install-recommends -y \  
git vim tmux \  
ros-kinetic-ros-core \  
ros-kinetic-rosserial-python \  
ros-kinetic-rosbridge-server \  
python-pip \  
python-dev \  
avahi-daemon \  
avahi-utils  
  
# clean system from unnecessary temp packages  
RUN apt-get autoclean -y && apt-get autoremove -y && apt-get clean -y && rm
-rf /var/lib/apt/lists/*  
  
# install request python module  
RUN pip install setuptools requests flask  
  
# clone project repository into home  
RUN git clone https://github.com/ludusrusso/pp-robot-2018.git  
  
# copy avahi configuration file  
COPY ./avahi-daemon.conf /etc/avahi/  
  
# workaround to get dbus working, required for avahi to talk to dbus. This
will be mounted  
RUN mkdir -p /var/run/dbus  
VOLUME /var/run/dbus  
  
# setup entrypoint  
COPY ./entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bash"]  


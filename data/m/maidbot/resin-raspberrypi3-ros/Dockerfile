FROM maidbot/resin-raspberrypi3-qemu  
  
MAINTAINER Spyros Maniatopoulos spyros@maidbot.co  
  
RUN [ "cross-build-start" ]  
  
# Switch on systemd init system in container and set various other variables  
ENV INITSYSTEM="on" \  
TERM="xterm" \  
ROS_DISTRO="indigo"  
RUN echo "deb http://packages.ros.org/ros/ubuntu trusty main" >
/etc/apt/sources.list.d/ros-latest.list \  
&& apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key
0xB01FA116  
  
RUN apt-get clean \  
&& apt-get update \  
&& apt-get install -yq --no-install-recommends --fix-missing \  
locales locales-all \  
python-dev python-pip \  
python-rosdep python-catkin-tools \  
ros-indigo-navigation ros-indigo-robot-localization ros-indigo-roslint \  
ros-indigo-hector-trajectory-server python-enum \  
python-rpi.gpio \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/lib/arm-linux-gnueabihf/liblog4cxx.so /usr/lib/  
  
RUN pip install platformio  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN rosdep init \  
&& rosdep update  
  
COPY ./ros_entrypoint.sh .  
  
RUN [ "cross-build-end" ]  
  
ENTRYPOINT ["bash", "ros_entrypoint.sh"]  
  
CMD ["bash"]  


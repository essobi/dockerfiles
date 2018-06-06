# raspbian stretch eed70f0cfc15 with ros
http://wiki.ros.org/action/fullsearch/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi  
# maintainer @urpylka 13122017  
FROM resin/rpi-raspbian:stretch-20171206  
RUN echo "Хорихоцский я оставлю тебя здесь"  
  
# less IIu3ДeTb  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup keys  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116  
  
# setup sources.list  
RUN echo "deb http://packages.ros.org/ros/ubuntu stretch main" >
/etc/apt/sources.list.d/ros-latest.list  
  
# install bootstrap tools  
RUN apt-get update && apt-get upgrade \  
&& apt-get install --no-install-recommends -y \  
wget \  
unzip \  
python-rosdep \  
python-rosinstall-generator \  
python-wstool \  
python-rosinstall \  
build-essential \  
cmake  
  
# setup environment  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# bootstrap rosdep  
RUN rosdep init \  
&& rosdep update  
  
# create catkin workspace  
RUN mkdir -p ~/ros_catkin_ws && cd ~/ros_catkin_ws \  
&& rosinstall_generator ros_comm --rosdistro kinetic --deps --wet-only --tar >
kinetic-ros_comm-wet.rosinstall \  
&& wstool init src kinetic-ros_comm-wet.rosinstall  
  
# Unavailable Dependencies  
RUN mkdir -p ~/ros_catkin_ws/external_src \  
&& cd ~/ros_catkin_ws/external_src \  
&& wget
http://sourceforge.net/projects/assimp/files/assimp-3.1/assimp-3.1.1_no_test_models.zip/download
-O assimp-3.1.1_no_test_models.zip \  
&& unzip assimp-3.1.1_no_test_models.zip \  
&& cd assimp-3.1.1 \  
&& cmake . \  
&& make \  
&& make install  
  
# Resolving Dependencies with rosdep  
RUN cd ~/ros_catkin_ws \  
&& rosdep install -y --from-paths src --ignore-src --rosdistro kinetic -r
--os=debian:stretch  
  
# Building the catkin Workspace  
RUN cd ~/ros_catkin_ws \  
&& ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release
--install-space /opt/ros/kinetic -j2  
  
# install ros packages  
ENV ROS_DISTRO kinetic  
  
# setup entrypoint  
COPY ./ros_entrypoint.sh /  
  
ENTRYPOINT ["/ros_entrypoint.sh"]  
CMD ["bash"]  


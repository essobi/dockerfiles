#  
# PX4 SITL and ROS featured apps container by JMGRobotics. Based on PX4 full
ROS container (https://hub.docker.com/r/px4io/px4-ros-full/~/dockerfile/)  
#  
################################################################################################################################################################  
#  
# Copyright (c) 2015, JMG Robotics LLC  
# All rights reserved.  
#  
# Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:  
#  
# 1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.  
#  
# 2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation  
# and/or other materials provided with the distribution.  
#  
# 3. Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from this
software without  
# specific prior written permission.  
#  
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED  
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY  
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS  
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING  
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  
#  
################################################################################################################################################################  
  
FROM ubuntu:14.04.3  
MAINTAINER Nuno Marques <n.marques21@hotmail.com>  
  
################################################################################################################################################################  
# Install basics  
## Use the "noninteractive" debconf frontend  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install wget git mercurial sudo  
  
################################################################################################################################################################  
# Prepare for automatic execution (not necessary if you execute the commands
manually one by one)  
RUN set -e \  
&& export DEBIAN_FRONTEND=noninteractive  
  
################################################################################################################################################################  
# Main ROS Setup  
# Following http://wiki.ros.org/indigo/Installation/Ubuntu  
# Also adding dependencies for gazebo
http://gazebosim.org/tutorials?tut=drcsim_install  
  
## add ROS repository and key  
## install main ROS pacakges  
RUN sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" >
/etc/apt/sources.list.d/ros-latest.list' \  
&& wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - |
sudo apt-key add - \  
&& sudo apt-get update \  
&& sudo apt-get -y install ros-indigo-desktop-full \  
&& sudo rosdep init \  
&& rosdep update  
  
## setup environment variables  
RUN sudo sh -c "echo 'source /opt/ros/indigo/setup.bash' >> ~/.bashrc" \  
&& exit \  
&& source ~/.bashrc \  
&& sudo bash  
  
## get rosinstall and some additional dependencies  
RUN sudo apt-get -y install python-rosinstall ros-indigo-octomap-msgs ros-
indigo-joy \  
ros-indigo-geodesy unzip ros-indigo-octomap-ros  
  
## install mavros but from shadow repo to get latest version earlier  
RUN sudo sh -c 'echo "deb http://packages.ros.org/ros-shadow-fixed/ubuntu/
trusty main" > /etc/apt/sources.list.d/ros-shadow.list' \  
&& sudo apt-get update \  
&& sudo apt-get -y install ros-indigo-mavros ros-indigo-mavros-extras  
  
################################################################################################################################################################  
# Install some utilities  
# x11-utils to get xdpyinfo, for X11 display debugging  
# mesa-utils provides glxinfo, handy for understanding the 3D support  
# jstest-gtk provides a graphical joystick testing and configuration tool  
RUN apt-get -y install x11-utils mesa-utils jstest-gtk  
  
################################################################################################################################################################  
# Install python tools  
  
# Install some Python Ubuntu packages  
RUN sudo apt-get -y install python-pip python-mock python-enum34 python-
protobuf \  
python-pandas python-numpy python-jinja2  
  
## Install Fuse support  
RUN sudo apt-get -y install fuse \  
&& pip install fusepy  
  
# Install some packages from source  
RUN mkdir -p python_src \  
&& cd python_src  
  
# Used to create graphs for web  
RUN git clone --branch px4_plots https://github.com/PX4/bearcart \  
&& cd bearcart \  
&& python setup.py install \  
&& cd ..  
  
# Used to create plots from rosbags  
RUN git clone https://github.com/aktaylor08/RosbagPandas \  
&& cd RosbagPandas \  
&& python setup.py install \  
&& cd ..  
  
RUN rm -rf python_src  
  
################################################################################################################################################################  
# ROS workspace setup  
  
RUN WDIR=`pwd` \  
&& WORKSPACE=$WDIR/catkin_ws  
  
# Setup workspace  
RUN mkdir -p $WORKSPACE/src \  
&& cd $WORKSPACE/src \  
&& exit \  
&& catkin_init_workspace \  
&& sudo bash \  
&& cd $WORKSPACE \  
&& catkin_make \  
&& sh -c "echo 'source $WORKSPACE/devel/setup.bash' >> ~/.bashrc"  
# Fetch sources  
## PX4 firmware  
RUN cd $WORKSPACE/src \  
&& git clone --recursive https://github.com/PX4/Firmware.git  
  
## rotors simulator  
RUN cd $WORKSPACE/src \  
&& git clone https://github.com/PX4/rotors_simulator.git  
  
## mav comm  
RUN cd $WORKSPACE/src \  
&& git clone https://github.com/PX4/mav_comm.git  
  
## glog catkin  
RUN cd $WORKSPACE/src \  
&& git clone https://github.com/ethz-asl/glog_catkin.git  
  
## catkin simple  
RUN cd $WORKSPACE/src \  
&& git clone https://github.com/catkin/catkin_simple.git  
  
# Disable parallel make jobs for compilation.  
# Sometimes required inside Docker container or VMs with not enough memory.  
# If you're on a native Ubuntu installation, you can leave this away.  
RUN export ROS_PARALLEL_JOBS=  
  
# Compile workspace  
RUN cd $WORKSPACE \  
&& exit \  
&& source devel/setup.bash \  
&& sudo bash \  
&& catkin_make  
  
################################################################################################################################################################  
# Some QT-Apps/Gazebo don't not show controls without this  
ENV QT_X11_NO_MITSHM 1  
  
################################################################################################################################################################  
# Run bash shell  
CMD ["/bin/bash"]  


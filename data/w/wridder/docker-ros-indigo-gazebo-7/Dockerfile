FROM ros:indigo  
MAINTAINER Wilbert van de Ridder wilbert.ridder+drig7@gmail.com  
  
# Arguments  
ARG user  
ARG uid  
ARG home  
ARG workspace  
ARG shell  
# Basic Utilities  
RUN apt-get -y update && apt-get install -y zsh screen tree sudo ssh synaptic  
  
# Latest X11 / mesa GL  
RUN apt-get install -y\  
xserver-xorg-dev-lts-wily\  
libegl1-mesa-dev-lts-wily\  
libgl1-mesa-dev-lts-wily\  
libgbm-dev-lts-wily\  
mesa-common-dev-lts-wily\  
libgles2-mesa-lts-wily\  
libwayland-egl1-mesa-lts-wily\  
libopenvg1-mesa  
  
# Dependencies required to build rviz  
RUN apt-get install -y\  
qt4-dev-tools\  
libqt5core5a libqt5dbus5 libqt5gui5 libwayland-client0\  
libwayland-server0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1\  
libxcb-render-util0 libxcb-util0 libxcb-xkb1 libxkbcommon-x11-0\  
libxkbcommon0  
  
# Make SSH available  
EXPOSE 22  
# Mount the user's home directory  
VOLUME "${home}"  
  
# Clone user into docker image and set up X11 sharing  
RUN \  
echo "${user}:x:${uid}:${uid}:${user},,,:${home}:${shell}" >> /etc/passwd && \  
echo "${user}:x:${uid}:" >> /etc/group && \  
echo "${user} ALL=(ALL) NOPASSWD: ALL" > "/etc/sudoers.d/${user}" && \  
chmod 0440 "/etc/sudoers.d/${user}"  
  
# install ros and gazebo packages  
RUN apt-get update && apt-get install -y \  
build-essential tree curl python-rosdep python-rosinstall-generator python-
wstool python-rosinstall wget \  
&& apt-get remove -y gazebo2 \  
&& rm /etc/ros/rosdep/sources.list.d/20-default.list  
  
# Additional development tools  
RUN apt-get install -y x11-apps python-pip build-essential  
RUN pip install catkin_tools  
  
# Install gazebo-ros packages  
RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable
`lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list' \  
&& wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
\\\  
&& apt-get update && apt-get install -y ros-indigo-gazebo7-ros-pkgs ros-
indigo-gazebo7-ros-control  
  
# Install additional ros packages  
RUN apt-get update && apt-get install -y ros-indigo-control-msgs ros-indigo-
forward-command-controller libeigen3-dev  
  
# Install Ruby dependencies  
RUN apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev python-software-properties libffi-dev  
  
# TODO: Install ruby itself.  
# Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Switch to user  
USER "${user}"  
# This is required for sharing Xauthority  
ENV QT_X11_NO_MITSHM=1  
ENV CATKIN_TOPLEVEL_WS="${workspace}/devel"  
# Switch to the workspace  
WORKDIR ${workspace}  


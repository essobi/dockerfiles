# Base container file to run Gazebo + ROS for CI and Simulated fleet of robots
with Docker.  
FROM ros:kinetic  
  
# allow ssh access from outside  
EXPOSE 22  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable
`lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'  
  
RUN apt-get update && apt-get install -y wget  
RUN wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add -  
RUN apt-get update && apt-get install -y gazebo7  
  
RUN apt-get update && apt-get -y install \  
ros-kinetic-desktop-full \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get -y install \  
javascript-common \  
libjs-jquery \  
libjs-sphinxdoc \  
libjs-underscore \  
python-catkin-lint \  
python-catkin-lint \  
python-catkin-tools \  
python-concurrent.futures \  
python-osrf-pycommon \  
python-trollius \  
ros-kinetic-gazebo-ros-control \  
ros-kinetic-gazebo-ros-control \  
ros-kinetic-gazebo-ros-pkgs \  
ros-kinetic-gazebo-ros-pkgs \  
ros-kinetic-geometry-msgs \  
ros-kinetic-joy \  
ros-kinetic-ros-control \  
ros-kinetic-ros-controllers \  
ros-kinetic-rosserial-arduino \  
ros-kinetic-web-video-server \  
ros-kinetic-serial \  
ros-kinetic-teleop-tools \  
ros-kinetic-teleop-twist-joy \  
ros-kinetic-xacro \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN easy_install pip  
  
RUN apt-get update && apt-get -y install \  
build-essential \  
python-rosinstall \  
python-rosinstall-generator \  
python-wstool \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get -y install \  
apt-utils \  
build-essential \  
curl \  
htop \  
repo \  
screen \  
ssh \  
tree \  
zsh \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN easy_install pip  
  
ENV LSCOLORS=Gxfxcxdxbxegedabagacad  
  
RUN rosdep update  
  
WORKDIR /catkin_ws  
  
CMD ["/bin/bash", "-c", "rosversion -d"] # only way to run ros stuff
https://forums.docker.com/t/bash-env-setup-scripts/15092/3  


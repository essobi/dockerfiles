FROM harmish/ros:indigo  
  
# install extra packages required by mummer  
RUN apt-get update && \  
apt-get install -y \  
libnlopt-dev \  
ros-indigo-naoqi-bridge \  
ros-indigo-nao-interaction \  
ros-indigo-octomap-msgs \  
ros-indigo-ros-control \  
ros-indigo-tf2\\* && \  
#  
# clean-up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  


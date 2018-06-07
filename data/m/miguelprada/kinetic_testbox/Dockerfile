FROM ros:kinetic  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN sed -i 's/#precedence ::ffff:0:0\/96 100/precedence ::ffff:0:0\/96 100/g'
/etc/gai.conf  
  
RUN apt-get update -qq \  
&& apt-get -qq install --no-install-recommends -y apt-utils wget ca-
certificates  
  
RUN apt-get update -qq \  
&& apt-get -qq install --no-install-recommends -y \  
build-essential \  
python-catkin-tools \  
python-pip \  
python-rosdep \  
python-wstool \  
ros-$ROS_DISTRO-catkin \  
ssh-client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y \  
ros-$ROS_DISTRO-angles \  
ros-$ROS_DISTRO-ros-control \  
ros-$ROS_DISTRO-ros-controllers  


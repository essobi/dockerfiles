FROM cogrob/omnimapper:dep  
  
# install build tools  
RUN apt-get install -y \  
cmake \  
cmake-curses-gui  
  
# install build libraries  
RUN apt-get install -y \  
libboost-all-dev \  
libflann-dev \  
libgsl0-dev \  
libgoogle-perftools-dev  
  
# install extra ros libraries  
RUN apt-get install -y \  
libeigen3-dev \  
ros-${ROS_DISTRO}-perception-pcl \  
ros-${ROS_DISTRO}-openni2-launch  


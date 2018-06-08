FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04  
MAINTAINER Zhiliang Zhou <zhouzhiliang@gmail.com>  
  
# Important  
# you need to install nvidia-docker,  
# and start container with nvidia-docker instead of docker  
# build setups follows indigo-ros-core -> indigo-ros-base -> indigo-desktop-
full  
# only difference is not based on ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup keys  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116  
  
# setup sources.list  
RUN echo "deb http://packages.ros.org/ros/ubuntu trusty main" >
/etc/apt/sources.list.d/ros-latest.list  
  
# install bootstrap tools  
RUN apt-get update && apt-get install --no-install-recommends -y \  
python-rosdep \  
python-rosinstall \  
python-vcstools \  
&& rm -rf /var/lib/apt/lists/*  
# setup environment  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# bootstrap rosdep  
RUN rosdep init \  
&& sudo rosdep update  
  
# install ros core packages  
ENV ROS_DISTRO indigo  
RUN apt-get update && apt-get install -y \  
ros-indigo-ros-core=1.1.5-0* \  
&& rm -rf /var/lib/apt/lists/*  
# install ros base packages  
RUN apt-get update && apt-get install -y \  
ros-indigo-ros-base=1.1.5-0* \  
&& rm -rf /var/lib/apt/lists/*  
# install ros desktop full packages  
RUN apt-get update && apt-get install -y \  
ros-indigo-desktop-full=1.1.5-0* \  
&& rm -rf /var/lib/apt/lists/*  
# setup entrypoint, need entrypoint.sh in the same folder with Dockerfile  
COPY ./ros_entrypoint.sh /  
  
ENTRYPOINT ["/ros_entrypoint.sh"]  
CMD ["bash"]  


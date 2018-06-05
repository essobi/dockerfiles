# Udacity capstone project dockerfile  
FROM ros:kinetic-robot  
LABEL maintainer="olala7846@gmail.com"  
  
# Install Dataspeed DBW https://goo.gl/KFSYi1 from binary  
# adding Dataspeed server to apt  
RUN sh -c 'echo "deb [ arch=amd64 ]
http://packages.dataspeedinc.com/ros/ubuntu $(lsb_release -sc) main" >
/etc/apt/sources.list.d/ros-dataspeed-public.list' && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FF6D3CDA && \  
sh -c 'echo "yaml http://packages.dataspeedinc.com/ros/ros-
public-'$ROS_DISTRO'.yaml '$ROS_DISTRO'" >
/etc/ros/rosdep/sources.list.d/30-dataspeed-public-'$ROS_DISTRO'.list'  
RUN rosdep update && \  
apt-get update && \  
apt-get install -y --no-install-recommends "ros-$ROS_DISTRO-dbw-
mkz=1.0.11-0xenial-20171020-111750-0400" \  
"ros-$ROS_DISTRO-cv-bridge=1.12.4-0xenial-20170613-183021-0800" \  
"ros-$ROS_DISTRO-pcl-ros=1.4.1-0xenial-20170727-185800-0800" \  
"ros-$ROS_DISTRO-image-proc=1.12.20-0xenial-20170613-192315-0800" \  
netbase \  
python-pip \  
ccache && \  
apt-get upgrade -y && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH /usr/lib/ccache/:$PATH  
  
# install python packages  
RUN pip install --no-cache-dir --upgrade "pip==9.0.1" && \  
pip install --no-cache-dir "Flask==0.11.1" \  
"attrdict==2.0.0" \  
"eventlet==0.19.0" \  
"python-socketio==1.6.1" \  
"numpy==1.13.1" \  
"Pillow==2.2.1" \  
"scipy==0.19.1" \  
"keras==2.0.8" \  
"tensorflow==1.3.0" \  
"h5py==2.6.0" \  
"pylint==1.7.4" \  
"matplotlib==2.1.0" && \  
mkdir -p /capstone && mkdir -p /root/.ccache  
  
VOLUME ["/capstone"]  
VOLUME ["/root/.ros/log/"]  
VOLUME ["/root/.ccache"]  
EXPOSE 4567  
WORKDIR /capstone/ros  


# This is an auto generated Dockerfile for ros:indigo-ros-base  
# generated from templates/docker_images/create_ros_image.Dockerfile.em  
# generated on 2017-01-27 02:33:52 +0000  
FROM ubuntu:14.04  
LABEL maintainer "JongYoon Lim<jongyoon@apache.org>"  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
  
# setup sources.list  
RUN echo "deb http://packages.ros.org/ros/ubuntu trusty main" >
/etc/apt/sources.list.d/ros-latest.list  
  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \  
python-rosdep \  
python-rosinstall \  
python-vcstools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# setup keys  
RUN apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key
0xB01FA116  
  
# setup sources.list  
RUN echo "deb http://packages.ros.org/ros/ubuntu trusty main" >
/etc/apt/sources.list.d/ros-latest.list  
  
# Fetch ROS package repo details  
RUN apt-get -y update  
  
# Install ROS  
RUN apt-get -y install ros-indigo-desktop-full  
  
# Install additional useful packages  
RUN apt-get -y install bash-completion git build-essential vim wget  
  
# bootstrap rosdep  
RUN rosdep init \  
&& rosdep update  
  
# Create a ROS workspace for the ROS user.  
RUN mkdir -p /root/catkin_ws/src  
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; catkin_init_workspace
/root/catkin_ws/src'  
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /root/catkin_ws;
catkin_make'  
RUN echo "source ~/catkin_ws/devel/setup.bash" >> /root/.bashrc  
  
RUN mkdir ~/opencv  
RUN cd ~/opencv && git clone https://github.com/Itseez/opencv_contrib.git &&
cd opencv_contrib && git checkout 3.2.0  
RUN cd ~/opencv && git clone https://github.com/Itseez/opencv.git && cd opencv
&& git checkout 3.2.0  
  
RUN cd ~/opencv/opencv && mkdir release && cd release && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \  
-D INSTALL_C_EXAMPLES=OFF \  
-D INSTALL_PYTHON_EXAMPLES=OFF \  
-D BUILD_EXAMPLES=OFF \  
-D WITH_OPENGL=ON \  
-D WITH_V4L=ON \  
-D WITH_XINE=ON \  
-D WITH_TBB=ON ..  
  
RUN cd ~/opencv/opencv/release && make -j $(nproc) && make install  
RUN wget -O /pylon-5.0.5.9000.tar.gz
"https://www.dropbox.com/s/7yxzyudgdukicme/pylon-5.0.5.9000--
RC8-x86_64.tar.gz?dl=0"  
RUN cd / && tar xzvf /pylon-5.0.5.9000.tar.gz  
RUN cd /pylon-5.0.5.9000-x86_64 && tar -C /opt -xzf pylonSDK*.tar.gz  
RUN cd /pylon-5.0.5.9000-x86_64 && yes | ./setup-usb.sh  
  
# setup entrypoint  
COPY ./ros_entrypoint.sh /  
RUN chmod +x /ros_entrypoint.sh  
ENTRYPOINT ["/ros_entrypoint.sh"]  
  
CMD ["bash"]  


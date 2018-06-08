FROM ubergarm/armhf-ubuntu:trusty  
  
ENV QEMU_EXECVE 1  
# Force armv6l  
# ENV QEMU_CPU arm1176  
COPY dockerutils/* /usr/bin/  
COPY sources.sh /tmp/  
  
RUN [ "cross-build-start" ]  
  
RUN /tmp/sources.sh  
RUN more /etc/apt/sources.list  
  
# Problem apt-gets  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libgsm1-dev \  
libboost-coroutine-dev \  
libboost-log-dev  
  
RUN apt-get install -y --no-install-recommends \  
git \  
emacs \  
build-essential \  
python-dev \  
g++ \  
python-smbus \  
i2c-tools \  
cmake \  
libusb-1.0-0-dev \  
autoconf \  
automake \  
libass-dev \  
libavdevice-dev \  
libfreetype6-dev \  
libsdl1.2-dev \  
libtheora-dev \  
libtool \  
libva-dev \  
libvdpau-dev \  
libvorbis-dev \  
libxcb1-dev \  
libxcb-shm0-dev \  
libxcb-xfixes0-dev \  
pkg-config \  
texinfo \  
zlib1g-dev \  
libcurl4-openssl-dev \  
libcurlpp-dev \  
libcurlpp0 \  
libjsoncpp-dev  
  
# FFmpeg  
RUN git clone https://github.com/FFmpeg/FFmpeg.git; \  
cd FFmpeg; git checkout tags/n3.1.3; \  
./configure; make; make install; cd ..; rm -rf FFmpeg;  
  
# This fixes roscd (maybe something to do with running ROS as root)  
# http://answers.ros.org/question/53353/autocomplete-not-working-
anymore/?comment=72208#comment-72208  
RUN echo "export LC_ALL="C"" >> ~/.bashrc  
  
# ROS Packages  
# Most packages are suites, but some should only be installed individually
because  
# of either the magnitude of their dependencies or the size of other nodes in
the suite.  
# Particularly, these should be kept individual installations:  
# roslint  
#  
RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" >
/etc/apt/sources.list.d/ros-latest.list  
RUN apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-key
0xB01FA116  
RUN apt-get clean && apt-get update && apt-get install -y --no-install-
recommends \  
ros-indigo-ros-base \  
ros-indigo-catkin \  
ros-indigo-roslint \  
ros-indigo-image-common \  
ros-indigo-diagnostics \  
ros-indigo-image-transport-plugins \  
ros-indigo-teleop-twist-joy \  
ros-indigo-razor-imu-9dof \  
ros-indigo-vision-opencv \  
ros-indigo-geometry \  
python-rosinstall \  
python-catkin-tools  
  
RUN rosdep init  
  
# Clean up installation files  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# switch to new user  
USER root  
WORKDIR /root  
  
# configure ROS (it will give Warning as our UID is same as root, 0)  
RUN echo "source /opt/ros/indigo/setup.bash" >> /root/.bashrc  
RUN echo "source /root/rowboat1/src/rowboat/devel/setup.bash" >> /root/.bashrc  
RUN bash -c "source /root/.bashrc && rosdep update"  
  
# Copy in git repo  
# COPY . /root/rowboat1  
# RUN git clone https://github.com/Seanmatthews/rowboat1.git  
RUN [ "cross-build-end" ]  
  
ENTRYPOINT [ "/usr/bin/qemu-arm-static", "/usr/bin/env", "QEMU_EXECVE=1" ]  
CMD [ "/bin/bash" ]  
  


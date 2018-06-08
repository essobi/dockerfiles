FROM ros:indigo-robot  
  
ENV LEONARDO 129.94.233.251  
  
RUN apt-get update && apt-get install -y \  
# build-essential \ # not sure how this is different  
g++ \  
cmake \  
make \  
ros-indigo-desktop-full \  
ros-indigo-ros-tutorials \  
ros-indigo-rqt \  
ros-indigo-rqt-common-plugins \  
tmux \  
i3 \  
vim \  
ssh \  
ros-indigo-rviz \  
ros-indigo-hokuyo-node \  
ros-indigo-openni2-launch \  
ros-indigo-image-transport \  
ros-indigo-image-transport-plugins \  
ros-indigo-pcl-ros \  
ros-indigo-libg2o \  
ros-indigo-rosdoc-lite \  
ros-indigo-map-server \  
libnewmat10-dev \  
freeglut3-dev \  
libsuitesparse-dev  
  
VOLUME /cs3431  
  
COPY .tmux.conf /root/  


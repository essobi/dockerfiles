FROM ros:indigo  
  
# install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update --no-install-recommends  
RUN apt-get -yq install --no-install-recommends ros-indigo-joy \  
ros-indigo-warehouse-ros \  
ros-indigo-gazebo-ros \  
ros-indigo-turtlebot \  
ros-indigo-turtlebot-gazebo \  
ros-indigo-hector-sensors-description \  
build-essential \  
ros-indigo-turtlebot-rviz-launchers  
  
RUN apt-get install -y --no-install-recommends mesa-utils \  
xserver-xorg-video-all \  
wget  
  
# setup ros and catkin  
#RUN rosdep -yq init  
RUN rosdep -yq update  
RUN /bin/bash -c "source /opt/ros/indigo/setup.bash && \  
mkdir -p ~/catkin_ws/src && \  
cd ~/catkin_ws/src && \  
catkin_init_workspace"  
  
RUN /bin/bash -c "source /opt/ros/indigo/setup.bash && \  
cd ~/catkin_ws/src && \  
git clone https://github.com/gtoff/icclab_turtlebot.git && \  
cd .. && \  
catkin_make"  
  
# setup entrypoint  
COPY ./ros_entrypoint.sh /  
RUN chmod +x /ros_entrypoint.sh  
  


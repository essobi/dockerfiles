# Note here for details http://www.ros.org/reps/rep-0142.html  
FROM ros:kinetic-perception  
  
RUN echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" >
/etc/apt/sources.list.d/ros-latest.list  
  
RUN apt-get update && apt-get install -y \  
vim \  
ros-kinetic-rosbridge-server \  
ros-kinetic-tf2-web-republisher \  
ros-kinetic-control-msgs \  
ros-kinetic-diagnostics \  
ros-kinetic-executive-smach \  
ros-kinetic-filters \  
ros-kinetic-geometry \  
ros-kinetic-robot-model \  
ros-kinetic-robot-state-publisher \  
ros-kinetic-xacro \  
python-catkin-tools \  
&& rm -rf /var/lib/apt/lists/*  
  
# I have changed this file  
COPY ros_entrypoint.sh /  
  
# Setting up the catkin workspace  
RUN mkdir -p /home/root/catkin_ws/src  
WORKDIR /home/root/catkin_ws  
RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash \  
&& catkin build"  
  
ENTRYPOINT ["/ros_entrypoint.sh"]  
CMD ["bash"]  


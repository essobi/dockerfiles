# davetcoleman/bolt:bolt-jade-source  
  
FROM moveit/moveit_docker:moveit-jade-source  
MAINTAINER Dave Coleman dave@dav.ee  
  
ENV CATKIN_WS=/root/ws_moveit  
WORKDIR $CATKIN_WS/src  
  
# delete old source code, download bolt source  
RUN cd .. && rm -rf src/ && mkdir src && cd src && \  
wstool init && \  
wstool merge https://raw.githubusercontent.com/davetcoleman/bolt/jade-
devel/bolt.jade.rosinstall && \  
wstool update  
  
# TEMPORARY until touch is added to moveit-jade-source  
RUN apt-get update && \  
apt-get install -y wget && \  
wget https://raw.githubusercontent.com/ros-gbp/ompl-
release/debian/kinetic/xenial/ompl/package.xml -O ompl/package.xml  
  
# disable packages that do not have proper dependencies  
RUN touch robotiq/robotiq_action_server/CATKIN_IGNORE && \  
touch robotiq/robotiq_c_model_control/CATKIN_IGNORE && \  
touch robotiq/robotiq_ethercat/CATKIN_IGNORE && \  
touch robotiq/robotiq_s_model_control/CATKIN_IGNORE && \  
touch robotiq/robotiq_joint_state_publisher/CATKIN_IGNORE && \  
touch universal_robot/ur_gazebo/CATKIN_IGNORE && \  
touch moveit/moveit_planners/ompl/CATKIN_IGNORE  
  
# update apt-get because osrf image clears this cache and download deps  
RUN apt-get update && \  
apt-get remove -y ros-${ROS_DISTRO}-ompl && \  
apt-get install -y \  
less \  
emacs \  
bash-completion \  
wmctrl \  
valgrind \  
gdb && \  
rosdep install -y \--from-paths . --ignore-src --rosdistro ${ROS_DISTRO} --as-
root=apt:false && \  
apt-get remove -y ros-${ROS_DISTRO}-ompl && \  
rm -rf /var/lib/apt/lists/*  


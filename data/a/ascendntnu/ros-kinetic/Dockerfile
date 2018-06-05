FROM ros:kinetic  
LABEL maintainer="ascendntnu.no"  
  
ENV ROS_WORKSPACE_PATH=/catkin_ws  
  
RUN apt-get update && apt-get install -y \  
curl \  
build-essential \  
ros-kinetic-mavros \  
ros-kinetic-mavros-extras \  
ros-kinetic-tf2 \  
libopencv-dev \  
python-opencv  
  
# Creating the catkin_ws/src folder  
RUN mkdir -p $ROS_WORKSPACE_PATH/src  
  
# Running catkin_init_workspace in catkin_ws/src  
RUN /ros_entrypoint.sh catkin_init_workspace $ROS_WORKSPACE_PATH/src  
  
# Go to new workspace source  
WORKDIR $ROS_WORKSPACE_PATH/src  
  
# Add ascend_msgs repo from github  
RUN mkdir -p ascend_msgs  
RUN curl -L https://api.github.com/repos/ascendntnu/ascend_msgs/tarball/v1.3 |
tar -xz -C ascend_msgs --strip-components=1  
  
# Set the default working directory  
WORKDIR $ROS_WORKSPACE_PATH  
  
# Create an initial build to add ascend_msgs to cache  
RUN /ros_entrypoint.sh catkin_make  
  
# Adding a default command to run if none is spesified.  
# This requires that an executable bash file is mounted  
# to /build.sh (default file contains catkin_make).  
# Note also that no files needs to be sourced as  
# /ros_entrypoint.sh is already the entrypoint.  
COPY build.sh /  
CMD [ "/build.sh" ]  


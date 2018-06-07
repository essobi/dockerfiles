FROM osrf/ros:kinetic-desktop-full-xenial  
  
# Arguments  
ARG user=ros  
ARG uid=1000  
ARG gid=1000  
#Build tools and other  
RUN apt-get update && \  
apt-get install sudo git python-wstool python-rosdep ninja-build zsh -y  
  
# Intel Graphics support  
RUN apt-get update && \  
apt-get -y install libgl1-mesa-glx libgl1-mesa-dri  
  
#Turtlebot packages  
RUN apt-get update && \  
apt-get install ros-kinetic-turtlebot ros-kinetic-turtlebot-apps \  
ros-kinetic-turtlebot-interactions ros-kinetic-turtlebot-simulator \  
ros-kinetic-kobuki-ftdi -y  
  
# Rosbridge for server communication  
RUN apt-get update && \  
apt-get install ros-kinetic-rosbridge-server -y  
  
# Move a launch file so that gazebo can find it  
RUN cp
/opt/ros/kinetic/share/turtlebot_navigation/launch/includes/gmapping/gmapping.launch.xml
\  
/opt/ros/kinetic/share/turtlebot_navigation/launch/includes/  
  
# Clone user to container, necessary to get X server access.  
RUN export uid="${uid}" gid="${gid}" && \  
groupadd -g "${gid}" "${user}" && \  
useradd -m -u "${uid}" -g "${user}" -s /bin/bash "${user}" && \  
passwd -d "${user}" && \  
usermod -aG sudo "${user}"  
  
# Enable access to graphics HW  
RUN adduser "${user}" video  
  
WORKDIR "/ros"  
  
# Add whole repository for build.  
ADD . "/ros"  
# Entrypoint  
ADD "./docker/ros_entrypoint.sh" "/ros_entrypoint.sh"  
  
# Update repositories  
RUN wstool update -t src --delete-changed-uris  
RUN chown -R "${user}:${user}" "/ros"  
  
USER "${user}"  
# Install deb dependencies.  
RUN rosdep update && \  
rosdep install --from-paths src --ignore-src -y -r  
  
# Build and install.  
SHELL ["/bin/bash", "-c"]  
RUN source "/opt/ros/kinetic/setup.bash" &&\  
catkin_make_isolated --install --use-ninja  
  
#Nvidia support  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
ENV PATH /usr/local/nvidia/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
# Make SSH available  
EXPOSE 22  
# Reduce image size  
RUN sudo rm -rf /var/lib/apt/lists/*  
  
# Run robot base launch as default  
CMD ["roslaunch", "robotslam_launcher", "robot_3dsensor.launch"]  
  
# Mount the user's home directory  
VOLUME "/host_home"  
VOLUME "/rosbag"  


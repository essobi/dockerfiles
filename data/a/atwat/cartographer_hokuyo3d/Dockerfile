FROM ros:kinetic  
  
RUN apt-get update -qq \  
&& apt-get install -y sudo python-wstool python-rosdep ninja-build \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY cartographer_hokuyo3d.rosinstall /catkin_ws/  
  
RUN mkdir /catkin_ws/src -p \  
&& cd /catkin_ws \  
&& wstool init --shallow src cartographer_hokuyo3d.rosinstall \  
&& src/cartographer/scripts/install_proto3.sh \  
&& rosdep update \  
&& apt-get update -qq \  
&& rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& bash -c "source /opt/ros/${ROS_DISTRO}/setup.bash; catkin_make_isolated
--install --install-space=/opt/ros/${ROS_DISTRO} \--use-ninja" \  
&& rm -rf /catkin_ws  
  
COPY . /catkin_ws/src/cartographer_hokuyo3d  
  
RUN mkdir /catkin_ws/src -p \  
&& cd /catkin_ws \  
&& bash -c "source /opt/ros/${ROS_DISTRO}/setup.bash; catkin_make_isolated
--install --install-space=/opt/ros/${ROS_DISTRO} \--use-ninja" \  
&& rm -rf /catkin_ws  
  
COPY slam.sh /  
  
CMD ["bash", "-c", "/slam.sh"]  


FROM timn/fedora-ros:f25-kinetic-desktop  
MAINTAINER Tim Niemueller <niemueller@kbsg.rwth-aachen.de>  
  
RUN /bin/bash -c "source /etc/profile; \  
mkdir -p /opt/ros/catkin_ws_${ROS_DISTRO}_desktopfull/src; \  
cd /opt/ros/catkin_ws_${ROS_DISTRO}_desktopfull; \  
rosinstall_generator desktop_full --rosdistro $ROS_DISTRO \--deps --wet-only
--tar --exclude RPP > $ROS_DISTRO-desktopfull.rosinstall; \  
wstool init -j $(nproc) src ${ROS_DISTRO}-desktopfull.rosinstall; \  
rosdep install --from-paths src --ignore-src --rosdistro $ROS_DISTRO -y; \  
catkin_make_isolated --install --install-space /opt/ros/$ROS_DISTRO \  
-DCMAKE_BUILD_TYPE=$ROS_BUILD_TYPE; \  
rm -rf *_isolated; \  
"  


FROM ros:kinetic  
  
RUN apt-get update -qq \  
&& apt-get install -y libusb-1.0-0 dkms libssl-dev libusb-1.0-0-dev linux-
headers-generic \  
&& apt-get download ros-kinetic-librealsense \  
&& dpkg --unpack ros-kinetic-librealsense*.deb \  
&& rm /var/lib/dpkg/info/ros-kinetic-librealsense.postinst -f \  
&& dpkg --configure ros-kinetic-librealsense \  
&& apt-get install -yf \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update -qq && apt-get install -y \  
ros-kinetic-turtlebot-gazebo \  
ros-kinetic-turtlebot-teleop ros-kinetic-turtlebot-rviz-launchers \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update -qq && apt-get install -y \  
ros-kinetic-depthimage-to-laserscan \  
ros-kinetic-yocs-cmd-vel-mux \  
ros-kinetic-kobuki-node \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update -qq && apt-get install -y \  
mesa-utils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY ps4_teleop.launch /opt/ros/kinetic/share/turtlebot_teleop/launch/  
  
VOLUME /root/  
  
CMD ["roslaunch", "turtlebot_gazebo", "turtlebot_world.launch"]  


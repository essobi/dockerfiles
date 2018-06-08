# This Docker file is used to encapsulate the Neato setup used in various  
# Olin College courses  
FROM ros:kinetic-perception  
MAINTAINER Paul Ruvolo Paul.Ruvolo@olin.edu  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV ROS_HOSTNAME=10.0.75.2  
# install ros packages  
RUN apt-get update && apt-get install -y \  
ros-kinetic-robot=1.3.0-0* \  
software-properties-common \  
wget \  
unzip \  
hping3 \  
x11vnc \  
xvfb \  
fvwm \  
tcpdump \  
net-tools \  
iputils-ping \  
python-pip \  
libgstreamer1.0-dev \  
libgstreamer-plugins-* \  
gstreamer1.0-libav* \  
gstreamer1.0-plugins* \  
ros-kinetic-turtlebot \  
ros-kinetic-turtlebot-apps \  
ros-kinetic-turtlebot-interactions \  
ros-kinetic-turtlebot-simulator \  
ros-kinetic-kobuki-ftdi \  
ros-kinetic-ar-track-alvar-msgs \  
vim && \  
setcap cap_net_raw+ep /usr/sbin/hping3 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup catkin workspace and ROS environment.  
RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash && \  
mkdir -p ~/catkin_ws/src && \  
cd ~/catkin_ws/src && \  
git clone -b qea https://github.com/paulruvolo/comprobo17.git && \  
git clone https://github.com/ros-teleop/teleop_twist_keyboard.git && \  
catkin_init_workspace && \  
cd ~/catkin_ws/ && \  
catkin_make && \  
echo 'source ~/catkin_ws/devel/setup.bash' >> ~/.bashrc"  
  
COPY xsession /root/.xsession  
  
# setup files required for x11vnc  
# To start the x11vnc server use: docker exec container_name x11vnc -forever
-usepw -create  
RUN /bin/bash -c "mkdir ~/.vnc && \  
mkdir ~/.rviz && \  
x11vnc -storepasswd 1234 ~/.vnc/passwd && \  
chmod u+x ~/.xsession"  
  
COPY default.rviz /root/.rviz  
  
CMD /bin/bash -c "source ~/catkin_ws/devel/setup.bash && roslaunch neato_node
bringup_minimal.launch host:=$HOST use_udp:=false"  


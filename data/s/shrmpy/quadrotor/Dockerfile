FROM osrf/ros:kinetic-desktop-full-xenial  
  
ARG VNC_PASSWORD=secret  
ENV VNC_PASSWORD=${VNC_PASSWORD} \  
DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update; apt-get install -y \  
dbus-x11 x11vnc xvfb supervisor \  
dwm suckless-tools stterm \  
build-essential \  
cmake \  
imagemagick \  
libboost-all-dev \  
libgts-dev \  
libjansson-dev \  
libtinyxml-dev \  
mercurial \  
nodejs \  
nodejs-legacy \  
npm \  
pkg-config \  
psmisc; \  
mkdir -p /etc/supervisor/conf.d; \  
x11vnc -storepasswd $VNC_PASSWORD /etc/vncsecret; \  
chmod 444 /etc/vncsecret; \  
adduser --system --home /home/gopher --shell /bin/bash --group --disabled-
password gopher; \  
usermod -a -G www-data gopher;  
  
# apt-get autoclean; \  
# apt-get autoremove; \  
# rm -rf /var/lib/apt/lists/*;  
  
COPY supervisord.conf /etc/supervisor/conf.d  
EXPOSE 5900  
ENTRYPOINT ["/usr/bin/env"]  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  
  
# Download quadrotor sim plugin  
RUN mkdir -p /root/catkin_ws/src; . /opt/ros/kinetic/setup.sh; \  
apt-get install -y ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-
keyboard ros-kinetic-geographic-msgs; \  
cd /root/catkin_ws; \  
rosinstall src /opt/ros/kinetic
https://raw.githubusercontent.com/AS4SR/hector_quadrotor/kinetic-
devel/tutorials.rosinstall; \  
. /root/catkin_ws/src/setup.sh; \  
rosdep install --from-path src --ignore-src --rosdistro kinetic --default-yes;
\  
catkin_make;  
  
#### . /root/catkin_ws/devel/setup.sh; roslaunch hector_quadrotor_demo
indoor_slam_gazebo.launch;  
# Build GZWeb  
RUN hg clone https://bitbucket.org/osrf/gzweb /root/gzweb; \  
cd /root/gzweb; hg up default; . /opt/ros/kinetic/setup.sh; \  
xvfb-run -s "-screen 0 1280x1024x24" ./deploy.sh -m local;  
EXPOSE 8080 7681  
  


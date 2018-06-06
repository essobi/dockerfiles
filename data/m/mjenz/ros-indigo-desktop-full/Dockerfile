FROM osrf/ros:indigo-desktop-full  
  
# Set apt mirror to ucmirror and install extra packages  
RUN sed -i
"s/http:\/\/archive.ubuntu.com/http:\/\/ucmirror.canterbury.ac.nz/g"
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \  
bash-completion \  
ros-indigo-rosbash \  
nano \  
psmisc && \  
rm -rf /var/lib/apt/lists/*  
# Sourcing this before .bashrc runs breaks ROS completions  
RUN echo "\nsource /opt/ros/indigo/setup.bash" >> /root/.bashrc  


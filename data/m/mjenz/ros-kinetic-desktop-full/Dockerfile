FROM osrf/ros:kinetic-desktop-full  
  
# Set apt mirror to ucmirror and install extra packages  
RUN sed -i
"s/http:\/\/archive.ubuntu.com/http:\/\/ucmirror.canterbury.ac.nz/g"
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \  
bash-completion \  
nano \  
tmux \  
ipython \  
ros-kinetic-rosbash \  
psmisc \  
python-scipy && \  
rm -rf /var/lib/apt/lists/*  
  
# Sourcing this before .bashrc runs breaks ROS completions  
RUN echo "\nsource /opt/ros/kinetic/setup.bash" >> /root/.bashrc  


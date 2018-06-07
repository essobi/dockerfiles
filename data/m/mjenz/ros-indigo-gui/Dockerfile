FROM mjenz/ros-indigo-desktop-full  
  
# Based on https://github.com/toddsampson/ros-docker/  
# See http://wiki.ros.org/docker/Tutorials/GUI  
  
ARG uid=1000  
ARG gid=1000  
  
RUN export uid=${uid} gid=${gid} && \  
groupadd -g ${gid} ros && \  
useradd -m -u ${uid} -g ros -s /bin/bash ros && \  
passwd -d ros && \  
usermod -aG sudo ros  
  
USER ros  
WORKDIR /home/ros  
  
# Sourcing this before .bashrc runs breaks ROS completions  
RUN echo "\nsource /opt/ros/indigo/setup.bash" >> /home/ros/.bashrc  
  
COPY ./ros_gui_entrypoint.sh /  
ENTRYPOINT ["/ros_gui_entrypoint.sh"]  
  


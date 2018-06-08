FROM ros:kinetic  
RUN /bin/bash -c "echo nameserver 8.8.8.8 > /etc/resolf.conf"  
RUN /bin/bash -c "echo nameserver 8.8.4.4 > /etc/resolf.conf"  
RUN apt-get update && apt-get install -y \  
sudo \  
python-catkin-tools \  
apt-utils \  
dialog \  
net-tools \  
iputils-ping  
RUN mkdir -p /home/ros/ros_ws/src  
RUN /bin/bash -c ". /opt/ros/kinetic/setup.bash; catkin_init_workspace
/home/ros/ros_ws/src"  
RUN git clone https://github.com/SalvoVirga/iiwa_stack.git
/home/ros/ros_ws/src/iiwa_stack  
RUN rosdep install --from-paths /home/ros/ros_ws/src --ignore-src -r -y  
RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash; \  
# source /home/ros/ros_ws/devel/setup.bash; \  
cd /home/ros/ros_ws; \  
catkin build"  
  
ENV ROS_MASTER_URI=http://192.168.2.100:11311  
EXPOSE 11311 80  


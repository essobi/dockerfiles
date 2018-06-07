FROM osrf/ros:indigo-desktop  
  
RUN apt-get update && apt-get install -q -y \  
ros-indigo-pepper-robot \  
ros-indigo-pepper-bringup \  
ros-indigo-pepper-description \  
ros-indigo-naoqi-pose \  
ros-indigo-find-object-2d \  
ros-indigo-keyboard \  
tmux \  
terminator \  
nano \  
emacs \  
gedit \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
  
RUN mkdir naoqi-sdk/  
RUN mkdir pynaoqi/  
  
ENV PYTHONPATH $PYTHONPATH:/root/pynaoqi/  
  
RUN echo "source /opt/ros/indigo/setup.bash" >> /root/.bashrc  
  
RUN mkdir -p catkin_ws/src  
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; catkin_init_workspace
/root/catkin_ws/src'  
RUN /bin/bash -c 'git clone https://github.com/ykoga-
kyutech/pepper_ros_handson.git /root/catkin_ws/src/pepper_ros_handson'  
RUN /bin/bash -c '. /opt/ros/indigo/setup.bash; cd /root/catkin_ws;
catkin_make'  
RUN echo "source /root/catkin_ws/devel/setup.bash" >> /root/.bashrc  
  
RUN echo "cd /root/catkin_ws/src/pepper_ros_handson; git pull origin master;
cd" >> /root/handson_update.sh  
  


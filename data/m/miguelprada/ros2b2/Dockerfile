FROM ros:kinetic  
  
RUN apt-get update && apt-get install -y -qq curl  
  
RUN curl http://repo.ros2.org/repos.key | apt-key add -  
  
RUN echo "deb http://repo.ros2.org/ubuntu/main xenial main" >
/etc/apt/sources.list.d/ros2-latest.list  
  
RUN apt-get update && apt-get install -y -qq ros-r2b2-*  
  
ENV ROS_DISTRO r2b2  


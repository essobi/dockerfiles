FROM virgiletn/ros-kinetic:light  
LABEL maintainer "virgile.dauge@inria.fr"  
  
#Clonning velodyne repository (getting last version)  
RUN git clone \  
https://github.com/ros-drivers/velodyne.git \  
/home/catkin_ws/src/velodyne/  
  
#Installing all required dependencies according to the source cloned before  
RUN apt-get -qq update \  
&& apt-get install -y \  
sudo \  
&& rosdep install --as-root apt:yes -r --from-paths /home/catkin_ws/ --ignore-
src --rosdistro kinetic -y \  
&& rm -rf /var/lib/apt/lists/*  
  
#Changing default shell for multi commands  
SHELL ["bin/bash", "-c"]  
  
#Compiling cloned sources  
RUN source /opt/ros/kinetic/setup.bash \  
&& cd /home/catkin_ws/ \  
&& catkin_make  
  
#Adding The required calibration File from same directory as dockerfile  
#ADD vlp16_calibration_file.yaml /home/  
#Or Adding it directly from github (needed for automatic build)  
ADD https://raw.githubusercontent.com/virgileTN/VLP16-utilities/master/ros-
kinetic-vlp16/vlp16_calibration_file.yaml /home/  
  
#Default command launching the node  
CMD cd /home/catkin_ws \  
&& source devel/setup.bash \  
&& roslaunch velodyne_pointcloud VLP16_points.launch
calibration:=/home/vlp16_calibration_file.yaml  


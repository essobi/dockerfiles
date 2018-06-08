# This is an auto generated Dockerfile for ros:desktop-full  
# generated from docker_images/create_ros_image.Dockerfile.em  
FROM osrf/ros:kinetic-desktop-xenial  
  
# install ros packages  
RUN apt-get update && apt-get install -y \  
ros-kinetic-desktop-full=1.3.1-0* \  
openssh-client python-catkin-tools ros-kinetic-controller-manager ros-kinetic-
catkin ros-kinetic-joint-state-controller ros-kinetic-gps-common libcgal-dev
libcgal-qt5-dev ros-kinetic-tf protobuf-compiler openssh-server curl tree
rsync git \  
&& rm -rf /var/lib/apt/lists/*  
  
#RUN apt-get update  
#RUN apt-get install -y openssh-client python-catkin-tools ros-kinetic-catkin
ros-kinetic-joint-state-controller ros-kinetic-gps-common ros-kinetic-tf
protobuf-compiler openssh-server curl tree rsync git  
ADD rab-sdk.tar.gz /home  
  
WORKDIR /home  
  
#RUN pwd  
#RUN ls -al  
#RUN ls -al host  
#RUN mv host rab-sdk  
#RUN ls -l rab-sdk  
#RUN mkdir -p /opt/husqvarna  
#RUN rsync -a -r rab-sdk/ /opt/husqvarna/rab-sdk  
RUN mv host rab-sdk && mkdir -p /opt/husqvarna && rsync -a -r rab-sdk/
/opt/husqvarna/rab-sdk  
  
RUN echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc  
  
ENTRYPOINT ["source ~/.bashrc"]  
CMD ["bash"]  
  
WORKDIR /opt/husqvarna/rab-sdk  
  
RUN ./relocate-sdk.sh


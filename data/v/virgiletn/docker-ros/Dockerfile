FROM virgiletn/docker-ros:indigo-rviz-intel  
LABEL maintainer "virgile.dauge@inria.fr"  
  
# install ros-kinetic-desktop-full  
RUN apt-get update \  
&& apt-get install -y \  
ros-kinetic-desktop-full \  
&& rm -rf /var/lib/apt/lists/*  
  
#Default command  
CMD ["bash"]  


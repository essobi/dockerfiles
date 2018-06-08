############################################  
  
# Dockerfile to build Ubuntu:14.04 \+ Gazebo5  
  
# + C/C++, Python dev libs image  
  
############################################  
  
# From inside this folder  
# docker build -t jorgeluisrmx/gazebo5  
# From DockerHub  
# docker pull jorgeluisrmx/gazebo5  
# Basic run  
# docker run -it jorgeluisrmx/gazebo5 /bin/bash  
  
FROM jorgeluisrmx/ubuntu-dev-base  
MAINTAINER jorgeluisrmx "jorgeluisrmx@gmail.com"  
  
RUN echo "deb http://packages.osrfoundation.org/gazebo/ubuntu trusty main" >
/etc/apt/sources.list.d/gazebo-latest.list  
  
RUN wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add
-  
  
RUN apt-get update  
  
RUN apt-get install -y gazebo5  


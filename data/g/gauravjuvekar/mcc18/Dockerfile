FROM ubuntu:trusty  
MAINTAINER Gaurav Juvekar <gauravjuvekar@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
binutils \  
git \  
scons \  
wget \  
cmake \  
build-essential \  
flex \  
bison \  
python-yaml \  
graphviz \  
lib32z1 \  
lib32ncurses5 \  
lib32bz2-1.0 \  
lib32stdc++6  
  
COPY mplabc18-v3.40-linux-full-installer.run /opt/  
RUN /opt/mplabc18-v3.40-linux-full-installer.run --mode unattended  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/opt:/opt/microchip/mplabc18/v3.40/bin  
  
COPY doxygen-1.8.10.src.tar.gz /  
RUN tar -xf doxygen-1.8.10.src.tar.gz  
RUN cd doxygen-1.8.10/ && mkdir build && cd build && cmake -G "Unix Makefiles"
.. && make install  
  
COPY plantuml.jar /opt/  
  
COPY fsusb /usr/local/bin/  


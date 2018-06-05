FROM centos:centos6  
MAINTAINER Andy Freeland <andy.freeland@redjack.com>  
  
# Development tools  
RUN yum groupinstall -y "Development Tools"  
RUN yum install -y cmake git sudo  
  
# The docker container has no tty  
RUN sed -i 's/^Defaults requiretty/#Defaults requiretty/' /etc/sudoers  
  
# Build/install buzzy  
RUN git clone \--recursive https://github.com/redjack/buzzy.git  
RUN mkdir buzzy/.build  
RUN cd buzzy/.build && cmake ..  
RUN cd buzzy/.build && make  
RUN cd buzzy/.build && ./src/buzzy install  


FROM ubuntu  
MAINTAINER cliffrowley@gmail.com  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y update && \  
apt-get install -q -y --no-install-recommends \  
libc6-i386  
  
USER root  
  
ENV QW_DIR=/qw  
  
RUN mkdir $QW_DIR  
  
WORKDIR $QW_DIR  
ADD files/qw/mvdsv $QW_DIR/mvdsv  
ADD files/qw/LICENSE $QW_DIR/LICENSE.mvdsv


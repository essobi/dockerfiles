FROM nvidia/cuda:8.0-devel-ubuntu16.04  
MAINTAINER Panos Nikolopoulos <p.nikolopoulos@quanticboost.com>  
  
ADD vm/dependencies.sh /usr/local/bin/dependencies.sh  
RUN chmod +x /usr/local/bin/dependencies.sh  
RUN /usr/local/bin/dependencies.sh  
  
ENV LC_ALL C.UTF-8  
VOLUME ["/data"]  
  
WORKDIR /data  
  


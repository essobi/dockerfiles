FROM ubuntu:14.04  
MAINTAINER James Johnson  
  
RUN apt-get update  
  
# We need a place to put our scripts  
RUN mkdir -p /usr/local/bin  
  
# Perform build-time configuration of the container  
ADD container-controller.configure /usr/local/bin/container-
controller.configure  
RUN chmod +x /usr/local/bin/container-controller.configure  
RUN /usr/local/bin/container-controller.configure  
  
# Install any other scripts  
ADD container-controller.start /usr/local/bin/container-controller.start  
  
# Override by adding '--entrypont /bin/bash' or similar to 'docker run'  
ENTRYPOINT ["/usr/local/bin/container-controller.start"]  


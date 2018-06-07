# ##  
# Docker: Factorio  
#  
# Builds a Docker image for running a Factorio server under Scales and
PufferPanel.  
#  
# Author: Steven Mirabito (steven@stevenmirabito.com)  
# ##  
FROM ubuntu:14.04  
MAINTAINER stevenmirabito <steven@stevenmirabito.com>  
  
RUN useradd -m -d /home/container container  
  
USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
CMD ["/bin/bash"]  


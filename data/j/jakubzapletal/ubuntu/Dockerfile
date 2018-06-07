FROM ubuntu:14.04  
  
MAINTAINER Jakub Zapletal <zapletal.jakub@gmail.com>  
  
# Install.  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y curl git wget nano  
  
# Add files.  
ADD scripts/.bashrc /root/.bashrc  
  
# Define volume  
VOLUME /data  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]


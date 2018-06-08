# Pull base image.  
FROM ubuntu:vivid  
MAINTAINER Erik Dasque <erik@frenchguys.com>  
  
# Install base packages  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# RUN apt-get install python-software-properties -y  
# RUN add-apt-repository ppa:rwky/redis  
# Get:3 http://archive.ubuntu.com/ubuntu/ vivid/universe redis-tools amd64
2:2.8.19-3 [75.7 kB]  
# Get:4 http://archive.ubuntu.com/ubuntu/ vivid/universe redis-server amd64
2:2.8.19-3 [311 kB]  
# RUN apt-get install apt-utils -y  
RUN apt-get install redis-server -y  
  
# Create a mountable volume  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
# Expose ports  
EXPOSE 6379  
  
# Define default command.  
CMD ["redis-server"]


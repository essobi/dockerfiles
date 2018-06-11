############################################################  
# Dockerfile to build MongoDB container images  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:xenial  
  
# File Author / Maintainer  
MAINTAINER UnbornX  
  
################## BEGIN INSTALLATION ######################  
# Install MongoDB Following the Instructions at MongoDB Docs  
# Ref: http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install package (.deb)  
RUN apt-get install -y vlc-nox nano sudo net-tools alsa-utils  
  
##################### INSTALLATION END #####################  
  
# Default port to execute the entrypoint ()  
CMD ["/bin/bash"]  
  
# Set default container command  
#ENTRYPOINT usr/bin/mongod  


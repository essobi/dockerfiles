# Baseline docker file for all docker images that are  
# supported on rethink testbed installations.  
#  
# Note: it is mandatroy, that ALL docker files for images  
# to be deployed on the rethink tesbed derive from this  
# image.  
FROM ubuntu:14.04  
MAINTAINER marc.emmelmann@fokus.fraunhofer.de  
  
# Create a /opt/reTHINK dir  
# all project specific stuff should be put in subdirectories (!!!)  
# below this path  
RUN apt-get update -y  
  
RUN mkdir /opt/reTHINK  


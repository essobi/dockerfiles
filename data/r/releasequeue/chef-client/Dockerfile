# Creating a Docker container containing Chef Client 12.x  
#  
# Start from Ubuntu 14.04.2  
#  
FROM ubuntu:14.04.2  
MAINTAINER Ringo De Smet <ringo@releasequeue.com>  
  
RUN apt-get -yqq update  
RUN apt-get -yqq install curl lsb-release  
RUN curl -L https://getchef.com/chef/install.sh | bash -s -- -v 12.0.3-1  
RUN apt-get -yqq clean  
  
# Make Chef available as a volume  
VOLUME /opt/chef  


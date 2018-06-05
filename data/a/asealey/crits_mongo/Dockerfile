#  
# Crits_Mongo Dockerfile  
# (Based on standard Docker provided Dockerfile)  
# https://github.com/dockerfile/mongodb  
#  
  
# Pull base image.  
FROM dockerfile/mongodb  
MAINTAINER Adam Sealey <asealey@gmail.com>  
  
# Set CRITs specified params for mongo  
# Not working because of Read-only filesystem  
# Known issue: https://github.com/docker/docker/issues/4717,
https://github.com/docker/docker/issues/5703  
# Parameters should be set at the host level  
#RUN echo 0 > /proc/sys/vm/zone_reclaim_mode  
  
# Define default command.  
ENTRYPOINT ["mongod","--logpath=/var/log/mongodb.log","--logappend"]  


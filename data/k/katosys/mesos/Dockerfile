#------------------------------------------------------------------------------  
# Set the base image for subsequent instructions:  
#------------------------------------------------------------------------------  
FROM quay.io/kato/mesos-base:v1.0.1-3  
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>  
  
#------------------------------------------------------------------------------  
# Environment variables:  
#------------------------------------------------------------------------------  
ENV DOCKER_VERSION="1.11.2"  
#------------------------------------------------------------------------------  
# Install mesos:  
#------------------------------------------------------------------------------  
RUN yum install -y wget && yum clean all && wget -q -O /tmp/docker.tgz \  
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz \  
&& tar zxvf /tmp/docker.tgz -C /tmp && find /tmp -type f -name docker \  
-exec cp {} /usr/local/bin \; && rm -rf /tmp/*  
  
#------------------------------------------------------------------------------  
# Command:  
#------------------------------------------------------------------------------  
CMD ["/bin/sh"]  


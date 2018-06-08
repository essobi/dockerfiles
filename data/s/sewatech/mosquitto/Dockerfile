FROM debian:jessie  
MAINTAINER Alexis Hassler <alexis@sewatech.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# see http://monkinetic.com/2014/07/25/docker-openstack-policy-rcd-mysqld  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
RUN apt-get update && \  
apt-get install -y mosquitto mosquitto-clients  
  
EXPOSE 1883  
CMD ["mosquitto"]  
  


FROM phusion/baseimage:0.9.22  
MAINTAINER Muhammad Kaisar Arkhan <yuki@coala.io>  
  
ENV DEBIAN_FRONTEND=noninteractive TERM=dumb \  
PLANET_DIRECTORY=/planet PLANET_CONFIG_FILE=/planet/planet.ini \  
PLANET_OUTPUT=/planet/output  
  
LABEL NAME=planet-venus \  
IMAGE_VERSION=1.0.1  
  
# Use the init system  
CMD /sbin/my_init  
  
# Install planet-venus and lighttpd  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
planet-venus \  
lighttpd \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy the files  
COPY . /  
  
# Make planet folder into a volume  
VOLUME $PLANET_DIRECTORY  
  
# Expose port 80  
EXPOSE 80  


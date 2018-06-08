FROM ubuntu:14.04.1  
MAINTAINER Gorka Lerchundi Osa <g.lerchundi@saltosystems.com>  
  
# Image name  
ENV IMAGE base  
  
# Set correct environment variables.  
ENV HOME /root  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
# Assets  
ADD assets /assets/$IMAGE  
RUN chmod +x /assets/$IMAGE/setup/install && \  
/assets/$IMAGE/setup/install && \  
rm -fr /assets/$IMAGE/setup  


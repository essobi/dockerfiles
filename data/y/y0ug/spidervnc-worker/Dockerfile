############################################################  
# Dockerfile to build Python WSGI Application Containers  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM y0ug/spidervnc-base  
  
# File Author / Maintainer  
MAINTAINER y0ug  
  
RUN apt-get update -yq && apt-get upgrade -yq  
  
ADD resources/etc/supervisor /etc/supervisor  
  
# Copy apps  
RUN wget -O - https://github.com/y0ug/spidervnc/archive/master.tar.gz | \  
tar xzf - -C /tmp/ && mv /tmp/spidervnc-master /var/app  
RUN pip install -r /var/app/requirements.txt  
  
EXPOSE 22  
  
VOLUME ['/var/log/', ]  
  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


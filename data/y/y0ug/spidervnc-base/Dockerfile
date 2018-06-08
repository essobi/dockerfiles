############################################################  
# Based on y0ug/base  
# Base stack for webvnc  
############################################################  
  
# Set the base image to Ubuntu  
FROM y0ug/base  
  
# File Author / Maintainer  
MAINTAINER y0ug  
  
# Update process  
RUN apt-get update -yq  
RUN apt-get upgrade -yq  
  
RUN apt-get install -yq git geoip-bin geoip-database libgeoip-dev libtiff5-dev
libjpeg-dev zlib1g-dev libfreetype6-dev vncsnapshot  
  
RUN wget -O /tmp/requirements.txt
https://raw.githubusercontent.com/y0ug/spidervnc/master/requirements.txt && \  
pip install -r /tmp/requirements.txt && \  
rm /tmp/requirements.txt  
  
  
ONBUILD RUN rm -rf /etc/ssh/ssh_host_* && ssh-keygen -A  
  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


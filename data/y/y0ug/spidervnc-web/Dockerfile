############################################################  
# Dockerfile to build Python WSGI Application Containers  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM y0ug/spidervnc-base  
  
# File Author / Maintainer  
MAINTAINER y0ug  
  
RUN apt-get update -yq && apt-get upgrade -yq  
RUN apt-get install -yq nginx uwsgi uwsgi-plugin-python  
  
RUN mkdir -p /run/uwsgi/app/webvnc/ && \  
chown www-data:www-data /run/uwsgi/app/webvnc/ && \  
rm -Rf /etc/nginx/sites-enabled && rm -Rf /etc/uwsgi/  
  
ADD resources/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD resources/etc/nginx/sites-enabled /etc/nginx/sites-enabled  
ADD resources/etc/uwsgi /etc/uwsgi  
ADD resources/etc/supervisor /etc/supervisor  
  
# Copy apps  
RUN wget -O - https://github.com/y0ug/spidervnc/archive/master.tar.gz | \  
tar xzf - -C /tmp/ && mv /tmp/spidervnc-master /var/app  
RUN pip install -r /var/app/requirements.txt  
  
EXPOSE 22  
EXPOSE 80  
  
VOLUME ['/var/log/', ]  
  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


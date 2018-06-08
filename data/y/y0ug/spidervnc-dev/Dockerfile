############################################################  
# Dockerfile to build Python WSGI Application Containers  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM y0ug/spidervnc-base  
  
# File Author / Maintainer  
MAINTAINER y0ug  
  
RUN apt-get install -yq rabbitmq-server mongodb nginx redis-server redis-tools  
RUN apt-get install -yq vim tmux ctags  
  
RUN sed -i 's/^daemonize yes/daemonize no/g' /etc/redis/redis.conf  
  
RUN rm /etc/nginx/sites-enabled/*  
ADD resources/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD resources/etc/nginx/sites-enabled /etc/nginx/sites-enabled  
ADD resources/etc/supervisor/ /etc/supervisor/  
  
RUN pip install flower  
  
RUN wget -O /tmp/requirements.txt
https://raw.githubusercontent.com/y0ug/spidervnc/master/requirements.txt && \  
pip install -r /tmp/requirements.txt && \  
rm /tmp/requirements.txt  
  
VOLUME [ "/var/app", "/var/lib/mongodb", ]  
  
EXPOSE 22  
EXPOSE 80  
EXPOSE 5672  
EXPOSE 6379  
EXPOSE 27017  
  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


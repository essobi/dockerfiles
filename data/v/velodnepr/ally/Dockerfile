############################################################  
# Dockerfile to run a Django-based web application  
# Based on an Ubuntu Image and Nginx  
############################################################  
  
# Set the base image to use to Nginx  
FROM ubuntu:16.04  
MAINTAINER Vladimir Yourtaev <yourtaev@gmail.com>  
  
ENV DJANGO_PRODUCTION=true  
  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y python3.5 python3-pip python3-dev nginx supervisor  
RUN pip3 install --upgrade pip  
  
RUN mkdir -p /opt/apps/media /opt/apps/static /opt/apps/log /opt/apps/code  
# VOLUME ["$DOCKYARD_SRVHOME/media/", "$DOCKYARD_SRVHOME/logs/"]  
  
ADD . /opt/apps/code  
  
# Install Python dependencies  
RUN pip3 install -r /opt/apps/code/requirements.txt  
  
  
# Configure Nginx  
RUN ln -s /opt/apps/code/nginx.conf /etc/nginx/sites-
enabled/django_docker.conf  
RUN rm /etc/nginx/sites-enabled/default  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
WORKDIR /opt/apps/code  
  
EXPOSE 8000  
  
# CMD ["/usr/bin/supervisord", "-e", "debug"]  
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]  
  


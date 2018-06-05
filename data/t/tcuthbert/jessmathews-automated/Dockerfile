############################################################  
# Dockerfile to run a Django-based web application  
# Based on an Ubuntu Image  
############################################################  
# Set the base image to use to Ubuntu  
FROM ubuntu:14.04  
# Set the file maintainer (your name - the file's author)  
MAINTAINER Thomas Cuthbert  
  
# Set env variables used in this Dockerfile (add a unique prefix, such as
DOCKYARD)  
# Local directory with project source  
ENV DOCKYARD_SRC=./app  
  
ENV VIRTUALHOST=jessmathews.com  
# Directory in container for all project files  
ENV DOCKYARD_SRVHOME=/srv  
# Directory in container for project source files  
ENV DOCKYARD_SRVPROJ=/srv/app  
  
# Update the default application repository sources list  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y python3 python3-dev python3-pip libpq-dev libjpeg8-dev  
  
# Create application subdirectories  
WORKDIR $DOCKYARD_SRVHOME  
RUN mkdir media static logs  
VOLUME ["$DOCKYARD_SRVHOME/media/", "$DOCKYARD_SRVHOME/logs/"]  
  
# Copy NGINX static location into static dir  
COPY ./default_location /static/  
  
# Copy application source code to SRCDIR  
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ  
  
# Install Python dependencies  
RUN pip3 install -r $DOCKYARD_SRVPROJ/requirements.txt  
  
# Port to expose  
EXPOSE 8000  
# Copy entrypoint script into the image  
WORKDIR $DOCKYARD_SRVPROJ  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  


############################################################  
# Dockerfile to run a Django-based web application  
# Based on an Ubuntu Image  
############################################################  
# Set the base image to use to Ubuntu  
FROM python:3  
# Set the file maintainer (your name - the file's author)  
MAINTAINER Gabriel Autes  
  
# Set env variables used in this Dockerfile (add a unique prefix, such as
DOCKYARD)  
# Local directory with project source  
ENV DOCKYARD_SRC=src  
# Directory in container for all project files  
ENV DOCKYARD_SRVHOME=/srv  
# Directory in container for project source files  
ENV DOCKYARD_SRVPROJ=/srv/topomat-lite  
  
# Update the default application repository sources list  
# RUN apt-get update && apt-get -y upgrade  
# RUN apt-get install -y python3.5 python-pip  
# Create application subdirectories  
WORKDIR $DOCKYARD_SRVHOME  
RUN mkdir logs  
VOLUME [ "$DOCKYARD_SRVHOME/logs/" ]  
  
# Copy application source code to SRCDIR  
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ  
  
# Install Python dependencies  
RUN pip install -r $DOCKYARD_SRVPROJ/requirements.txt  
  
# Port to expose  
EXPOSE 8000  
# Copy entrypoint script into the image  
WORKDIR $DOCKYARD_SRVPROJ  
COPY ./docker-entrypoint.sh /  
  
RUN chgrp -R 0 $DOCKYARD_SRVPROJ && \  
chmod -R g=u $DOCKYARD_SRVPROJ  
RUN ls -l ./  
ENTRYPOINT ["/docker-entrypoint.sh"]  


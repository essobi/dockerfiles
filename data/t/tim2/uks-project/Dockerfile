# Set the base image to use to Ubuntu  
FROM ubuntu:14.04  
# Set the file maintainer (your name - the file's author)  
MAINTAINER Jozef Kovac  
  
# Set env variables used in this Dockerfile (add a unique prefix, such as
DOCKYARD)  
# Local directory with project source  
ENV DOCKYARD_SRC=src  
# Directory in container for all project files  
ENV DOCKYARD_SRVHOME=/srv  
# Directory in container for project source files  
ENV DOCKYARD_SRVPROJ=/srv/uks-project  
  
# Update the default application repository sources list  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y python3-pip python python3-dev mysql-client
libmysqlclient-dev  
  
RUN apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev \  
libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk  
  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:git-core/ppa -y  
RUN apt-get update  
RUN apt-get install git -y  
RUN ln -s -T /usr/include/freetype2/ /usr/include/freetype  
  
# Create application subdirectories  
WORKDIR $DOCKYARD_SRVHOME  
RUN mkdir media static logs assets  
VOLUME ["$DOCKYARD_SRVHOME/media/", "$DOCKYARD_SRVHOME/logs/"]  
  
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


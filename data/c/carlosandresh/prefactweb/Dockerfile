FROM python:latest  
# FROM alpine  
# RUN apk add --update netcat python3 py3-pip gcc python3-dev py3-cffi file
git curl autoconf automake py3-cryptography linux-headers musl-dev libffi-dev
openssl-dev build-base  
# Set the file maintainer (your name - the file's author)  
LABEL MAINTAINER="Carlos Herrera"  
  
# Set env variables used in this Dockerfile (add a unique prefix, such as
DOCKYARD)  
# Local directory with project source  
ENV DOCKYARD_SRC=Prefact  
# Directory in container for all project files  
ENV DOCKYARD_SRVHOME=/srv  
# Directory in container for project source files  
ENV DOCKYARD_SRVPROJ=/srv/Prefact  
  
# Create application subdirectories  
WORKDIR $DOCKYARD_SRVHOME  
RUN mkdir media static logs  
# VOLUME ["$DOCKYARD_SRVHOME/media/", "$DOCKYARD_SRVHOME/logs/"]  
RUN mkdir web  
WORKDIR $DOCKYARD_SRVHOME/web  
RUN mkdir static  
  
VOLUME ["$DOCKYARD_SRVHOME/media/",
"$DOCKYARD_SRVHOME/logs/","$DOCKYARD_SRVHOME/web/static"]  
  
# Copy application source code to SRCDIR  
# COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ  
# WORKDIR $DOCKYARD_SRVPROJ  
# RUN git clone https://github.com/Carlos4ndresh/Prefact.git  
# ADD . $DOCKYARD_SRVPROJ/  
# Install Python dependencies  
# RUN pip install -r $DOCKYARD_SRVPROJ/Prefact/requirements.txt  
# Port to expose  
# EXPOSE 8000  
# Copy entrypoint script into the image  
WORKDIR $DOCKYARD_SRVPROJ/Prefact  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]


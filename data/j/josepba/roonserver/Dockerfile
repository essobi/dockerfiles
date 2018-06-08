# Dockerfile to prepare the latest version of RoonServer for Linux x86_64  
# Using latest alpine  
FROM frolvlad/alpine-glibc:latest  
  
# Inspired by mikedickey's' Dockerfile at
https://hub.docker.com/r/mikedickey/roonserver/  
# and instructions from http://kb.roonlabs.com/LinuxInstall  
MAINTAINER josep@iti.es  
  
# Location of Roon's latest Linux installer  
ENV ROON_SERVER_PKG RoonServer_linuxx64.tar.bz2  
ENV ROON_SERVER_URL http://download.roonlabs.com/builds/${ROON_SERVER_PKG}  
  
# These are expected by Roon's startup script  
ENV ROON_DATAROOT /var/roon  
ENV ROON_ID_DIR /var/roon  
  
# Create install dir, and Install prerequisite packages  
RUN mkdir /rooninstall \  
&& apk update \  
&& apk add bash curl bzip2 ffmpeg cifs-utils alsa-utils alsa-lib  
  
# Grab server to run it  
ADD ${ROON_SERVER_URL} /rooninstall  
ADD roon_initial_installer.sh /rooninstall  
# Fix installer permissions  
RUN chmod 700 /rooninstall/roon_initial_installer.sh  
  
# Your Roon data will be stored in /var/roon; /music is for your music,
/opt/RoonStuff for Roon itself  
VOLUME [ "/var/roon", "/music" , "/opt/RoonStuff"]  
  
# This starts Roon when the container runs, installing it for the first time
if need be  
ENTRYPOINT /rooninstall/roon_initial_installer.sh  


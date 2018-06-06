# Create a build and development environment for bitcoin  
#  
# Docker base for building coin daemons  
#  
FROM ubuntu:12.10  
MAINTAINER dasher  
  
# deal with installation warnings  
ENV TERM xterm  
# allow easy versioning of images  
ENV TESTING 0.2.0  
RUN apt-get update  
RUN apt-get install -y aptitude  
RUN aptitude -y upgrade  
  
# Upstart and DBus have issues inside docker. We work around that.  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
#&& ln -s /bin/true /sbin/initctl  
# Basic build dependencies.  
RUN aptitude install -y build-essential libtool autotools-dev autoconf libssl-
dev unzip yasm zip pkg-config checkinstall  
  
# Libraries required for building.  
RUN aptitude install -y libdb5.1-dev libdb5.1++-dev libboost-all-dev  
  
# Gold linker is much faster than standard linker.  
RUN apt-get install -y binutils-gold  
  
# Developer tools.  
RUN apt-get install -y bash-completion curl emacs git man-db python-dev
python-pip vim  
  
# Now let's build bitcoin  
VOLUME /data/buildOutput  
WORKDIR /home  
RUN mkdir development  
WORKDIR /home/development  


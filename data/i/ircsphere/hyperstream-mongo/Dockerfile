FROM ubuntu:16.04  
  
MAINTAINER Kacper Sokol <ks1591@bristol.ac.uk>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER root  
RUN apt-get update \  
&& apt-get upgrade -y  
  
RUN apt-get install -y \  
mongodb  
  
  
ENV SHELL /bin/bash  
ENV HYPERSTREAM_USER jovyan  
ENV HYPERSTREAM_UID 1000  
ENV HOME /home/$HYPERSTREAM_USER  
ENV HYPERSTREAM_DIR $HOME/hyperstream  
  
# Create jovyan user with UID=1000 and in the 'users' group \ -N -u $SWISH_UID  
RUN useradd -m -s $SHELL $HYPERSTREAM_USER  
RUN mkdir -p $HYPERSTREAM_DIR \  
&& chown $HYPERSTREAM_USER $HYPERSTREAM_DIR  
USER $HYPERSTREAM_USER  
#RUN wget
https://data.bris.ac.uk/datasets/8gccwpx47rav19vk8x4xapcog/8gccwpx47rav19vk8x4xapcog.zip  
  
EXPOSE 27017  
  
#RUN service mongod start  
ENTRYPOINT /usr/bin/mongod --smallfiles --dbpath "$HYPERSTREAM_DIR"  


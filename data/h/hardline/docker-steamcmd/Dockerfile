FROM ubuntu:xenial  
  
MAINTAINER Nicolas Favre <favre.nicolas.dotfr@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN dpkg --add-architecture i386  
RUN apt-get update -q  
RUN apt-get install -yqq ca-certificates  
RUN echo debconf steam/question select I AGREE | debconf-set-selections  
RUN apt-get install -yqq steamcmd  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/usr/games/steamcmd"]  
ONBUILD ENTRYPOINT []


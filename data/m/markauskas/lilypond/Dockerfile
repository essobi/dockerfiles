FROM ubuntu:xenial  
MAINTAINER Tomas Markauskas <tomas@markauskas.lt>  
  
RUN locale-gen en_US.UTF-8 && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure
locales  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update  
RUN apt-get -y install lilypond  


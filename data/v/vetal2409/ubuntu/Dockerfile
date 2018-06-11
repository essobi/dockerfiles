FROM ubuntu:16.04  
  
MAINTAINER Vitalii Sydorenko <vetal.sydo@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install dependency  
RUN apt-get update \  
&& apt-get install -y software-properties-common python-software-properties \  
&& apt-get install -y language-pack-en-base  
RUN LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php  
  
RUN apt-get update \  
&& apt-get install -y nano curl zip unzip  


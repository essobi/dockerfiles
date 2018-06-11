FROM ubuntu:16.04  
MAINTAINER Nguyen Anh Tien <nguyen.anh.tien@framgia.com>  
  
RUN DEBIAN_FRONTEND=noninteractive  
# Install "software-properties-common" (for the "add-apt-repository")  
RUN apt-get update && apt-get install -y \  
software-properties-common locales  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
RUN apt-get update && apt-get install -y --force-yes curl  
  
# Install Nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g typescript eslint yarn  


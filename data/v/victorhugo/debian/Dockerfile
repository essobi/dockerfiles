FROM debian:jessie  
MAINTAINER VictorHugo <victorhugo.avila.cl@gmail.com>  
  
# Disable interactive functions  
#ENV DEBIAN_FRONTEND noninteractive  
# Updating the SO and Installing useful tools  
RUN apt-get update && apt-get install -y \  
vim \  
wget \  
git \  
unzip \  
rpm \  
debconf \  
debconf \  
git  
  
# Configuring Locales  
COPY locale.gen /etc/locale.gen  
COPY locale.conf /etc/locale.conf  
#RUN locale-gen -> This command has problems.  
# Cleaning the apt/list repo  
RUN rm -rf /var/lib/apt/lists/*  


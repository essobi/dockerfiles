FROM ubuntu:16.04  
MAINTAINER JJ Lau <j.y.j.j.lau@gmail.com>  
LABEL description="Meteor Development Environment for TEDxUNSW"  
  
## INSTALL REQUIRED TOOLS  
RUN apt-get update && \  
apt-get install -y curl language-pack-en && \  
apt-get autoclean && \  
apt-get clean && \  
apt-get remove && \  
rm -Rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## SET ENVIRONMENT VARIABLES  
ENV METEOR_ALLOW_SUPERUSER=1  
## ADD NEW USER + INSTALL METEOR  
RUN useradd --create-home --shell /bin/bash tedxunsw \  
&& echo 'tedxunsw:everythingisawesome' | chpasswd \  
&& curl https://install.meteor.com | sh \  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -Rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## LOGIN AS NEW USER  
USER tedxunsw  
  
WORKDIR /home/tedxunsw  
  
## HACK TO DOWNLOAD METEOR PACKAGES  
RUN meteor logout  
  
EXPOSE 3000  


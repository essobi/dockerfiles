FROM debian:wheezy-slim  
MAINTAINER Alexei Smirnov <alexei@virtuman.com>  
  
ENV TZ=UTC \  
LANG=en_US.utf8 \  
TERM=xterm-256color \  
DEBIAN_FRONTEND=noninteractive \  
  
NODE_ENV=production \  
METEOR_ALLOW_SUPERUSER=true \  
PATH=$PATH:/home/${APP_USER}/.meteor \  
# Customization options  
PORT=3000 \  
  
APP_UID=1000 \  
APP_GID=1000 \  
APP_USER=node \  
APP_GROUP=node \  
  
RUN_AS_USER=nobody  
  
  
RUN mkdir /app_src && \  
apt-get update && \  
apt-get install -yqq curl g++ make nano procps python sudo && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/* /root/ngx* /opt/* /var/tmp/* /tmp/*  
  
WORKDIR /app_src  
  
  
ENV METEOR_RELEASE=1.4.1.1  
  
RUN echo "Installing Meteor v.${METEOR_RELEASE} ... " && \  
curl "https://install.meteor.com/?release=${METEOR_RELEASE}" | sh  
  
  
ENTRYPOINT []  
CMD []  


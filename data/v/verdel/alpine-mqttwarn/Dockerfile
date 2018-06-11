FROM verdel/alpine-base:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
ENV MQTTWARNINI /etc/mqttwarn/mqttwarn.ini  
  
# Install transmission and pushnotify  
RUN apk --update add --virtual build-dependencies git \  
&& pip install --upgrade pip \  
&& pip install --upgrade paho-mqtt \  
&& git clone https://github.com/jpmens/mqttwarn.git /opt/mqttwarn  
  
RUN apk del build-dependencies \  
&& rm -rf \  
/usr/share/man \  
/tmp/* \  
/var/cache/apk/*  
  
# Copy init scripts  
COPY rootfs /  


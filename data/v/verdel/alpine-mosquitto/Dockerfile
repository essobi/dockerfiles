FROM verdel/alpine-base:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
ENV MOSQUITTO_CONF_DIR /etc/mosquitto  
  
# Install transmission and pushnotify  
RUN apk --update add \  
mosquitto \  
# Clean up  
&& rm -rf \  
/usr/share/man \  
/tmp/* \  
/var/cache/apk/*  
  
# Copy init scripts  
COPY rootfs /  
  
# Expose ports  
EXPOSE 1883/tcp  


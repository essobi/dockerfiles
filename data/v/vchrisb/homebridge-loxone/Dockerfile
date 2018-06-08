  
FROM node:latest  
  
MAINTAINER Chris Banck  
  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies and tools  
RUN apt-get update; \  
apt-get install -y libnss-mdns avahi-discover libavahi-compat-libdnssd-dev
libkrb5-dev jq;  
  
# Install latest Homebridge  
# -------------------------------------------------------------------------  
# You can force a specific version by setting HOMEBRIDGE_VERSION  
# See https://github.com/marcoraddatz/homebridge-docker#homebridge_version  
RUN npm install -g homebridge --unsafe-perm  
  
RUN npm install -g homebridge-loxone-ws  
  
COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf  
  
USER root  
RUN mkdir -p /var/run/dbus  
ADD run.sh /root/run.sh  
ADD config.json /root/.homebridge/config.json  
  
# Run container  
EXPOSE 5353 51826  
CMD ["/root/run.sh"]  


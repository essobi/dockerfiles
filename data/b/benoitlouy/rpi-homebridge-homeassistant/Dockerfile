FROM resin/armv7hf-debian-qemu  
MAINTAINER Benoit Louy <benoit.louy@fastmail.com>  
  
VOLUME /config  
  
RUN [ "cross-build-start" ]  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
RUN apt-get install -y g++ git make nodejs libavahi-compat-libdnssd-dev avahi-
daemon avahi-discover && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV HOMEBRIDGE_V 0.4.20  
RUN npm install -g --unsafe-perm homebridge@${HOMEBRIDGE_V} hap-nodejs node-
gyp  
RUN cd /usr/lib/node_modules/homebridge && \  
npm install --unsafe-perm bignum  
RUN cd /usr/lib/node_modules/hap-nodejs/node_modules/mdns && \  
node-gyp BUILDTYPE=Release rebuild  
ENV HOMEBRIDGE_HASS_V 2.1.0  
RUN npm config set unsafe-perm true && \  
npm install -g homebridge-homeassistant@${HOMEBRIDGE_HASS_V}  
  
RUN mkdir -p /var/run/dbus  
ADD run.sh /root/run.sh  
  
RUN [ "cross-build-end" ]  
  
CMD [ "/root/run.sh" ]  


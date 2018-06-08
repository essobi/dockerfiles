FROM node  
  
RUN apt-get update && \  
apt-get install -yq libavahi-compat-libdnssd-dev && \  
apt-get install -yq apt-utils apt-transport-https && \  
apt-get install -yq libnss-mdns avahi-discover libavahi-compat-libdnssd-dev
libkrb5-dev && \  
rm -rf /var/lib/apt/lists/*  
  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc
/tini.asc  
RUN gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
&& gpg --verify /tini.asc  
RUN chmod +x /tini  
  
RUN npm install -g --unsafe-perm homebridge && \  
npm install -g --unsafe-perm homebridge-homeassistant  
  
# RUN apk add --no-cache tini python make g++ libffi-dev openssl-dev avahi-dev
avahi-compat-libdns_sd openrc dbus  
ENV HOMEBRIDGE_VERSION 0.4.33  
ENV HOMEBRIDGE_HOMEASSISTANT_VERSION 3.0.2  
RUN yarn global add node-gyp  
RUN yarn global add homebridge@$HOMEBRIDGE_VERSION homebridge-
homeassistant@$HOMEBRIDGE_HOMEASSISTANT_VERSION  
  
RUN adduser --disabled-password homebridge && \  
mkdir /config && \  
chown -R homebridge:homebridge /config  
VOLUME /config  
  
RUN mkdir -p /var/run/dbus  
VOLUME /var/run/dbus  
  
EXPOSE 5353 51826  
USER homebridge  
  
ENTRYPOINT ["/tini", "--"]  
CMD ["homebridge","-U","/config"]  


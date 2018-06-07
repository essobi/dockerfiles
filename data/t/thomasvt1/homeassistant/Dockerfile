# Set the base image  
FROM lsiobase/alpine  
  
# Dockerfile author / maintainer  
MAINTAINER Thomas <thomasvt@me.com>  
  
# Update application repository list and install the HASS server.  
RUN apk add --no-cache git python3 ca-certificates libffi-dev libssl1.0
libressl-dev && \  
pip3 install --upgrade --no-cache-dir pip && \  
apk add --no-cache --virtual=build-dependencies build-base linux-headers
python3-dev tzdata && \  
pip3 install --no-cache-dir homeassistant && \  
pip3 install --no-cache-dir home-assistant-frontend sqlalchemy==1.2.2 python-
miio==0.3.9 HAP-python==1.1.7 PyXiaomiGateway==0.8.3 distro==1.2.0
aiohttp_cors==0.6.0 jsonrpc-async==0.6 pychromecast==2.0.0 paho-mqtt==1.3.1
rxv==0.5.1 jsonrpc-websocket==0.6 websocket-client==0.37.0 && \  
apk del build-dependencies && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/*  
  
  
# Expose default port  
EXPOSE 8123  
  
CMD ["hass"]  


FROM alpine:3.6  
  
LABEL maintainer="jaeyeol@gmail.com"  
RUN apk update && \  
apk upgrade && \  
apk add python3 && \  
pip3 install --upgrade homeassistant && \  
pip3 install sqlalchemy mutagen phue && \  
apk add \--update build-base linux-headers python3-dev nodejs nodejs-npm nmap
&& \  
pip3 install netdisco psutil && \  
mkdir -p /config && \  
apk del build-base linux-headers python3-dev  
  
CMD /usr/bin/hass -c /config  
  


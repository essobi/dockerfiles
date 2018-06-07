FROM node:slim  
MAINTAINER Holger Imbery <contact@connectedobjects.cloud>  
LABEL version="1.0" \  
description="homekit2mqtt"  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
wget \  
libavahi-compat-libdnssd-dev \  
dbus \  
avahi-daemon \  
node-gyp \  
make \  
g++ \  
build-essential \  
avahi-discover \  
libnss-mdns \  
&& rm -rf /var/lib/apt/lists/*  
  
  
RUN npm install -g homekit2mqtt \  
\--unsafe-perm  
  
USER root  
RUN mkdir -p /var/run/dbus  
ADD entrypoint.sh /root/entrypoint.sh  
RUN chmod 755 /root/entrypoint.sh  
  
EXPOSE 5353 51888 51826  
VOLUME /root/homekit2mqtt  
ENTRYPOINT ["/root/entrypoint.sh"]  


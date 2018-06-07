FROM node  
MAINTAINER Jason Harmon <jason.harmon@gmail.com>  
  
ADD . /root/  
RUN apt-get update && \  
apt-get install -y curl wget libavahi-compat-libdnssd-dev dbus avahi-daemon
node-gyp make g++ build-essential avahi-discover libnss-mdns && \  
sed -i.bak 's/^#enable-dbus/enable-dbus/' /etc/avahi/avahi-daemon.conf && \  
yarn global add homebridge homebridge-homeassistant && \  
apt-get remove -y node-gyp make g++ build-essential  
  
USER root  
  
VOLUME /root/.homebridge/  
  
EXPOSE 5353 51826  
ENTRYPOINT ["/bin/sh", "/root/run.sh"]  


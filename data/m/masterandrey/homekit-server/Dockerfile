FROM nodesource/jessie:6.7.0  
MAINTAINER masterandrey "masterandrey@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive \  
TERM xterm  
  
RUN apt-get update && \  
apt-get install -y apt-utils apt-transport-https && \  
apt-get upgrade -y && \  
apt-get install -y locales curl wget nano vim xterm \  
libnss-mdns avahi-discover libavahi-compat-libdnssd-dev libkrb5-dev && \  
npm install -g homebridge --unsafe-perm && \  
mkdir -p /var/run/dbus && \  
mkdir -p /root/.homebridge/plugins && \  
mkdir -p /opt/hap-nodejs  
  
WORKDIR /opt/hap-nodejs  
COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf  
COPY homebridge /root/.homebridge/  
COPY run.sh /root/run.sh  
  
RUN chmod +x /root/run.sh && \  
git clone https://github.com/KhaosT/HAP-NodeJS.git . && \  
npm install && \  
npm install mqtt && \  
npm install mosca bunyan -g --unsafe-perm  
  
EXPOSE 51825 51825 \  
1883 1883  
CMD ["/root/run.sh"]  


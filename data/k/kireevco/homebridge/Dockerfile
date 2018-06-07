FROM node:7  
MAINTAINER Dmitry Kireev <dmitry@kireev.co>  
  
##################################################  
# Set environment variables #  
##################################################  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
##################################################  
# Install tools #  
##################################################  
  
RUN apt-get update && \  
apt-get install -y \  
apt-utils \  
apt-transport-https \  
locales \  
curl \  
wget \  
git \  
python \  
build-essential \  
make \  
g++ \  
libavahi-compat-libdnssd-dev \  
libkrb5-dev \  
vim \  
net-tools \  
nano  
  
##################################################  
# Install homebridge #  
##################################################  
  
RUN npm install -g homebridge \  
homebridge-philipshue \  
homebridge-ninjablock-temperature \  
homebridge-ninjablock-humidity \  
homebridge-ninjablock-alarmstatedevice \  
homebridge-luxtronik2 \  
homebridge-people \  
homebridge-mqttswitch \  
homebridge-edomoticz \  
homebridge-philipshue \  
homebridge-liftmaster \  
homebridge-ifttt \  
homebridge-nest \  
homebridge-homeassistant \  
homebridge-foscamcamera \  
# homebridge-wink \  
\--unsafe-perm  
  
##################################################  
# Start #  
##################################################  
  
USER root  
RUN mkdir -p /var/run/dbus  
  
ADD start.sh /root/start.sh  
  
VOLUME /root/.homebridge  
EXPOSE 5353 51826  
CMD ["/root/start.sh"]  


FROM node:8-alpine  
  
# inspired by https://github.com/iobroker/docker-iobroker  
MAINTAINER Patrick Eichmann <phreakazoid@phreakazoid.com>  
  
# Install required dependencies for the adapters  
# git: needed to download beta adapters  
# avahi-dev: needed by mdns (iobroker.chromecast)  
# make gcc g++ python linux-headers udev: needed by serialport
(iobroker.discovery) - https://www.npmjs.com/package/serialport#platform-
support  
RUN apk add --no-cache \  
bash python build-base \  
git \  
avahi-dev \  
make gcc g++ python linux-headers udev \  
tzdata  
  
# Install base iobroker  
RUN mkdir -p /opt/iobroker/  
WORKDIR /opt/iobroker/  
RUN npm install -g npm@>=5.7.1  
RUN npm install iobroker --unsafe-perm  
  
ADD scripts/* /usr/local/bin/  
  
#Delete data folder so it gets generated on the first boot  
#This is needed in order to associate the instances to the correct hostname  
#I would have preferred to build the container with hostname=iobroker but this  
#does not seem to be possible  
RUN rm -rf iobroker-data/*  
  
#Adding the line bellow results in a LOT of copies when starting the container  
#VOLUME /opt/iobroker  
#The iobroker_data has to be preserved across updates  
VOLUME /opt/iobroker/iobroker-data  
  
EXPOSE 8081 8082 8083 8084  
ENTRYPOINT ["run.sh"]  
CMD ["start"]  


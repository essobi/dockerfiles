ARG BASE=node:8-slim  
FROM $BASE  
  
ARG arch=arm  
ENV ARCH=$arch  
  
COPY qemu/qemu-$ARCH-static* /usr/bin/  
  
# inspired by https://github.com/iobroker/docker-iobroker  
MAINTAINER Vegetto <git@angelnu.com>  
  
# Install required dependencies for the adapters  
# git: needed to download beta adapters  
# avahi-dev: needed by mdns (iobroker.chromecast)  
# make gcc g++ python linux-headers udev: needed by serialport
(iobroker.discovery) - https://www.npmjs.com/package/serialport#platform-
support  
#RUN apk add --no-cache \  
# build-base avahi-dev linux-headers \  
RUN apt-get update && apt-get install -y \  
libavahi-compat-libdnssd-dev 'linux-headers-*' vim \  
bash python \  
git \  
make gcc g++ python udev \  
tzdata && \  
apt-get -y clean all  
  
#Update npmjs  
RUN npm config set unsafe-perm true #See https://github.com/npm/uid-
number/issues/3  
RUN npm install -g npm@latest  
  
# Install base iobroker  
RUN mkdir -p /opt/iobroker/  
WORKDIR /opt/iobroker/  
RUN npm install iobroker --unsafe-perm  
  
#Install adapters listed by adapters2install.json and add admin  
ADD adapters2install.json adapters2install.json  
RUN mv package.json package.json.org && \  
cp -a adapters2install.json package.json && \  
npm install --production --save --unsafe-perm --prefix /opt/iobroker  
  
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


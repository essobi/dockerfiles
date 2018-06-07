FROM resin/raspberrypi3-node:6  
# inspired by https://github.com/Locke/docker-iobroker  
MAINTAINER Jakob Westhoff <jakob@westhoffswelt.de>  
  
RUN [ "cross-build-start" ]  
  
RUN mkdir -p /opt/iobroker/ && chmod 777 /opt/iobroker  
WORKDIR /opt/iobroker/  
  
ADD Support/run.sh run.sh  
  
RUN npm install iobroker --unsafe-perm && \  
echo $(hostname) > .install_host && \  
chmod +x run.sh  
  
RUN [ "cross-build-end" ]  
  
VOLUME /opt/iobroker/  
EXPOSE 8081  
CMD /opt/iobroker/run.sh  


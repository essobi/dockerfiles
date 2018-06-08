FROM ubuntu:14.04.2  
MAINTAINER minimum@cepave.com  
  
ENV WORKDIR=/home/transfer PACKDIR=/package PACKFILE=falcon-transfer.tar.gz
CONFIGDIR=/config CONFIGFILE=cfg.json  
  
# Volume  
VOLUME $CONFIGDIR $WORKDIR $PACKDIR  
  
# Install Open-Falcon Transfer Component  
COPY $CONFIGFILE $CONFIGDIR/  
COPY $PACKFILE $PACKDIR/  
  
WORKDIR /root  
COPY run.sh ./  
  
# Port  
EXPOSE 6060 8433  
# Start  
CMD ["./run.sh"]  


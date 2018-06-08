FROM ubuntu:14.04.2  
MAINTAINER minimum@cepave.com  
  
ENV WORKDIR=/home/fe PACKDIR=/package PACKFILE=falcon-fe.tar.gz
CONFIGDIR=/config CONFIGFILE=cfg.json  
  
# Volume  
VOLUME $CONFIGDIR $WORKDIR $PACKDIR  
  
# Install Open-Falcon Fe Component  
COPY $CONFIGFILE $CONFIGDIR/  
COPY $PACKFILE $PACKDIR/  
  
WORKDIR /root  
COPY run.sh ./  
  
# Port  
EXPOSE 1234  
# Start  
CMD ["./run.sh"]  


FROM ubuntu:14.04.2  
MAINTAINER minimum@cepave.com  
  
ENV WORKDIR=/home/query PACKDIR=/package PACKFILE=falcon-query.tar.gz
CONFIGDIR=/config CONFIGFILE=cfg.json  
  
# Volume  
VOLUME $CONFIGDIR $WORKDIR $PACKDIR  
  
# Install Open-Falcon Query Component  
COPY $CONFIGFILE $CONFIGDIR/  
COPY $PACKFILE $PACKDIR/  
  
WORKDIR /root  
COPY run.sh ./  
  
# Port  
EXPOSE 9966  
# Start  
CMD ["./run.sh"]  


FROM ubuntu:14.04.2  
MAINTAINER minimum@cepave.com  
  
ENV WORKDIR=/home/hbs PACKDIR=/package PACKFILE=falcon-hbs.tar.gz
CONFIGDIR=/config CONFIGFILE=cfg.json  
  
# Volume  
VOLUME $CONFIGDIR $WORKDIR $PACKDIR  
  
# Install Open-Falcon HBS Component  
COPY $CONFIGFILE $CONFIGDIR/  
COPY $PACKFILE $PACKDIR/  
  
WORKDIR /root  
COPY run.sh ./  
  
# Port  
EXPOSE 6030 6031  
# Start  
CMD ["./run.sh"]  
  


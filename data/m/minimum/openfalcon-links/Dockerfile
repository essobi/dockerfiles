FROM ubuntu:14.04.2  
MAINTAINER minimum@cepave.com  
  
ENV WORKDIR=/home/links PACKDIR=/package PACKFILE=falcon-links.tar.gz
CONFIGDIR=/config CONFIGFILE=config.py  
  
# Volume  
VOLUME $CONFIGDIR $WORKDIR $PACKDIR  
  
# Install Open-Falcon Links Component  
RUN \  
apt-get update && \  
apt-get install -y python-virtualenv python-dev python-mysqldb  
COPY $CONFIGFILE $CONFIGDIR/  
COPY $PACKFILE $PACKDIR/  
  
WORKDIR /root  
COPY run.sh ./  
  
# Port  
EXPOSE 5090  
# Start  
CMD ["./run.sh"]  


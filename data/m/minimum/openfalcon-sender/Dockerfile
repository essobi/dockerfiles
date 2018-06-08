FROM ubuntu:14.04.2  
MAINTAINER minimum@cepave.com  
  
ENV WORKDIR=/home/sender PACKDIR=/package PACKFILE=falcon-sender.tar.gz
CONFIGDIR=/config CONFIGFILE=cfg.json  
  
# Volume  
VOLUME $CONFIGDIR $WORKDIR $PACKDIR  
  
# For QQ Message  
RUN \  
apt-get update && \  
apt-get install -y curl jq  
  
# Install Open-Falcon Sender Component  
COPY $CONFIGFILE $CONFIGDIR/  
COPY $PACKFILE $PACKDIR/  
  
WORKDIR /root  
COPY run.sh ./  
  
# Port  
EXPOSE 6066  
# Start  
CMD ["./run.sh"]  


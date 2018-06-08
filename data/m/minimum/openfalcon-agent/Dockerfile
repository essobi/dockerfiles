FROM ubuntu:14.04  
MAINTAINER minimum@cepave.com  
  
ENV WORKDIR=/home/agent PACKDIR=/package PACKFILE=falcon-agent.tar.gz
CONFIGDIR=/config CONFIGFILE=cfg.json  
  
# Volume  
VOLUME $CONFIGDIR $WORKDIR $PACKDIR  
  
# Install Open-Falcon Agent Component  
RUN apt-get update && apt-get install -y git  
COPY $CONFIGFILE $CONFIGDIR/  
COPY $PACKFILE $PACKDIR/  
  
WORKDIR /root  
COPY run.sh ./  
  
# Port  
EXPOSE 1988  
# Start  
CMD ["./run.sh"]  


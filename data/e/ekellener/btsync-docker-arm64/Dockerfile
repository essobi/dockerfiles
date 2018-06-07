FROM docker.io/project31/aarch64-alpine-qemu:3.5-7  
RUN [ "cross-build-start" ]  
  
MAINTAINER Erik Kellener (erik@kellener.com)  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
########## BTSYNC ##########  
RUN apk add --update bash curl jq  
  
RUN curl -o /usr/bin/btsync.tar.gz https://download-
cdn.resilio.com/stable/linux-armhf/resilio-sync_armhf.tar.gz  
RUN cd /usr/bin; tar xvzf btsync.tar.gz; rm btsync.tar.gz;  
RUN ln -s /usr/bin/rslsync /usr/bin/btsync  
  
WORKDIR /btsync  
  
ADD run_btsync.sh run_btsync.sh  
ADD config.json config.json  
RUN mkdir /btsync/storage  
  
EXPOSE 55555  
# Arguments Passed: DIR SECRET  
ENTRYPOINT ["/bin/bash", "run_btsync.sh"]  
RUN [ "cross-build-end" ]  


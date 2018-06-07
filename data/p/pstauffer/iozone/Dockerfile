FROM alpine:3.3  
  
MAINTAINER pstauffer@confirm.ch  
  
RUN apk \--update upgrade && \  
apk add \--no-cache \--virtual=temporary curl gcc make build-base && \  
curl http://www.iozone.org/src/current/iozone3_434.tar > /tmp/iozone.tar && \  
cd /tmp && \  
tar -xf /tmp/iozone.tar && \  
cd /tmp/iozone*/src/current && \  
make linux && \  
cp iozone /usr/bin/iozone && \  
apk del temporary && \  
rm -rf /var/cache/apk/* /tmp/iozone*  
  
CMD /bin/sh  


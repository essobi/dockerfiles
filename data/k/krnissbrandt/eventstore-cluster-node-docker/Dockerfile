FROM ubuntu:16.04  
MAINTAINER Kristofer Nissbrandt <nissbran@gmail.com>  
  
## INSTALLATION START ##  
ENV ES_VERSION=4.0.0  
RUN apt-get update && apt-get install curl -y &&\  
curl -s https://packagecloud.io/install/repositories/EventStore/EventStore-
OSS/script.deb.sh | bash &&\  
apt-get install eventstore-oss=$ES_VERSION -y &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## INSTALLATION ENDS ##  
## INTERNAL CLUSTER PORTS ##  
EXPOSE 1112  
EXPOSE 2112  
## EXTERNAL CLUSTER PORTS ##  
EXPOSE 1113  
EXPOSE 2113  
VOLUME /data/db  
VOLUME /data/logs  
VOLUME /certs  
  
COPY eventstore.conf /etc/eventstore/  
  
ENTRYPOINT ["eventstored"]  


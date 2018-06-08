FROM debian:jessie  
  
MAINTAINER tetsuobe  
  
ENV ES_VERSION 3.5.0  
ENV NOTVISIBLE "in users profile"  
RUN apt-get update -y && apt-get install curl -y  
RUN curl http://download.geteventstore.com/binaries/EventStore-OSS-
Ubuntu-14.04-v$ES_VERSION.tar.gz | tar xz -C /opt  
  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
ENV EVENTSTORE_EXT_HTTP_PORT 2113  
ENV EVENTSTORE_EXT_TCP_PORT 1113  
ENV EVENTSTORE_LOG /data/logs  
ENV EVENTSTORE_DB /data/db  
  
ENV EVENTSTORE_MAX_MEM_TABLE_SIZE 100000  
ENV EVENTSTORE_WORKER_THREADS 12  
ENV EVENTSTORE_RUN_PROJECTIONS All  
ENV EVENTSTORE_EXT_IP 0.0.0.0  
EXPOSE $EVENTSTORE_EXT_HTTP_PORT  
EXPOSE $EVENTSTORE_EXT_TCP_PORT  
  
VOLUME $EVENTSTORE_LOG  
VOLUME $EVENTSTORE_DB  
  
WORKDIR /opt/EventStore-OSS-Ubuntu-14.04-v$ES_VERSION  
  
CMD ./run-node.sh --ext-http-prefixes=http://*:$EVENTSTORE_EXT_HTTP_PORT/
--int-http-prefixes=http://*:$EVENTSTORE_EXT_HTTP_PORT/


# EventStore (geteventstore.com)  
#  
# VERSION 0.0.4  
# docker build -t eventstore/geteventstore:3.8.1 .  
# docker images  
# docker run -d -p 2113:2113 -p 1113:1113 eventstore/geteventstore:3.8.1  
# docker run -d --name anstelPreprod -p 2113:2113 -p 1113:1113 -v
/home/ugo/eventstore/db:/data/db -v /home/ugo/eventstore/logs:/data/logs
eventstore/geteventstore:3.8.1  
FROM ubuntu:14.04  
MAINTAINER Ugo Bourdon <bourdon.ugo@gmail.com>  
  
RUN apt-get update && apt-get install -y curl  
  
RUN curl http://download.geteventstore.com/binaries/EventStore-OSS-
Ubuntu-14.04-v3.8.1.tar.gz | tar xz -C /opt  
  
EXPOSE 2113  
EXPOSE 1113  
VOLUME ["/data/db", "/data/logs"]  
  
ENV EVENTSTORE_MAX_MEM_TABLE_SIZE 100000  
ENV EVENTSTORE_WORKER_THREADS 12  
WORKDIR /opt/EventStore-OSS-Ubuntu-14.04-v3.8.1  
  
ENTRYPOINT ["./run-node.sh", "--db=/data/db", "--log=/data/logs", "--run-
projections=all"]  
CMD ["--int-http-prefixes=http://*:2113/", "--ext-ip=0.0.0.0"]  


#  
# HEDventures EventStore Docker Container  
#  
# Example usage: docker run -d -p 1113:1113 -p 2113:2113 -v /host/db:/data/db
-v /host/logs:/data/logs hedventures/eventstore  
#  
FROM ubuntu  
  
MAINTAINER HEDventures Pty Ltd <hedteam@hedventures.com>  
  
RUN apt-get update && apt-get install -y curl  
  
RUN curl http://download.geteventstore.com/binaries/EventStore-OSS-
Linux-v3.0.5.tar.gz | tar xz -C /opt  
  
EXPOSE 1113  
EXPOSE 2113  
VOLUME /data/db  
VOLUME /data/logs  
  
ENV EVENTSTORE_WORKER_THREADS 12  
ENV EVENTSTORE_MAX_MEM_TABLE_SIZE 100000  
WORKDIR /opt/EventStore-OSS-Linux-v3.0.5  
  
CMD ./run-node.sh \  
\--ext-ip=$ES_HOST \  
\--ext-tcp-port=1113 \  
\--ext-http-port=2113 \  
\--http-prefixes=http://*:2113/ \  
\--db /data/db \  
\--log /data/logs \  
\--run-projections=all  
  
#  
# End  
#  


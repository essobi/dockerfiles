# Dockerfile for EventStore  
# http://geteventstore.com/  
FROM debian:jessie  
  
MAINTAINER Lukasz Golebiewski  
  
# Install curl  
RUN apt-get update && apt-get install -y curl  
  
# Create user  
RUN addgroup eventstore \  
&& adduser --ingroup eventstore --disabled-password --gecos "Database"
eventstore \  
&& usermod -L eventstore  
  
# Set environment variables  
USER eventstore  
ENV ES_VERSION 3.3.0  
ENV ES_HOME /opt/EventStore-OSS-Ubuntu-v$ES_VERSION  
ENV EVENTSTORE_DB /data/db  
ENV EVENTSTORE_LOG /data/logs  
  
# Download and extract EventStore  
USER root  
RUN curl http://download.geteventstore.com/binaries/EventStore-OSS-
Ubuntu-v$ES_VERSION.tar.gz | tar xz --directory /opt \  
&& chown -R eventstore:eventstore $ES_HOME  
  
# Add volumes  
RUN mkdir -p $EVENTSTORE_DB && mkdir -p $EVENTSTORE_LOG \  
&& chown -R eventstore:eventstore $EVENTSTORE_DB $EVENTSTORE_LOG  
VOLUME $EVENTSTORE_DB  
VOLUME $EVENTSTORE_LOG  
  
# Change working directory  
WORKDIR $ES_HOME  
  
# Fix "exec format error"  
RUN sed -i '1 c #!/bin/bash' run-node.sh  
  
# Expose the HTTP and TCP ports  
EXPOSE 2113 1113  
# Clean up.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Run  
ENTRYPOINT ["./run-node.sh"]  
CMD ["--ext-ip=0.0.0.0", "--ext-http-prefixes=http://*:2113/", "--run-
projections=all"]  


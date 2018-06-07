# Dockerfile for EventStore  
# http://geteventstore.com/  
FROM debian:jessie  
  
MAINTAINER Wadim Kruse <wadim.kruse@gmail.com>  
  
# Install curl  
RUN apt-get update && apt-get install -y curl  
  
# Create user  
RUN addgroup eventstore \  
&& adduser --ingroup eventstore --disabled-password --gecos "Database"
eventstore \  
&& usermod -L eventstore  
  
# Set environment variables  
USER eventstore  
ENV ES_VERSION 3.0.1  
ENV ES_HOME /opt/EventStore-OSS-Linux-v$ES_VERSION  
ENV EVENTSTORE_DB /data/db  
ENV EVENTSTORE_LOG /data/logs  
  
# Download and extract EventStore  
USER root  
RUN curl http://download.geteventstore.com/binaries/EventStore-OSS-
Linux-v$ES_VERSION.tar.gz | tar xz --directory /opt \  
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
  
# Run  
ENTRYPOINT ["./run-node.sh"]  
CMD ["--help"]  
  
# Expose the HTTP and TCP ports  
EXPOSE 2113 1113  
# Clean up.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


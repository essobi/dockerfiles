FROM openjdk:8-jre-alpine  
  
# Build variables  
ARG FLUME_VERSION="1.7.0"  
ARG SINK_VERSION=1.0.3  
# Environment variables  
ENV FLUME_AGENT_NAME "agent"  
ENV FLUME_CONFIG_PATH "/opt/flume/conf"  
ENV FLUME_CONFIG_FILE "/opt/flume/conf/agent.properties"  
ENV OPTIONS ""  
WORKDIR /opt/flume  
  
# Install flume  
ADD http://archive.apache.org/dist/flume/$FLUME_VERSION/apache-
flume-$FLUME_VERSION-bin.tar.gz /tmp  
RUN \  
tar --strip-components 1 -xzf /tmp/apache-flume-$FLUME_VERSION-bin.tar.gz && \  
rm -f /tmp/apache-flume-$FLUME_VERSION-bin.tar.gz && \  
rm -f lib/httpcore* && \  
rm -f lib/httpclient*  
  
# Copy configuration files  
COPY conf/ conf/  
  
# Copy all plugins  
COPY target/flume-elasticsearch-sink-$SINK_VERSION-jar-with-dependencies.jar
plugins.d/flume-rest/lib/  
  
RUN apk update && apk add bash && rm -rf /var/cache/apk/*  
  
# Create flume user and switch to it  
RUN adduser flume -h /opt/flume -s /bin/false -D flume  
RUN chown -R flume /opt/flume/conf  
USER flume  
  
EXPOSE 4141 34545 5445  
CMD exec /opt/flume/bin/flume-ng agent -n $FLUME_AGENT_NAME -c
$FLUME_CONFIG_PATH -f $FLUME_CONFIG_FILE $OPTIONS  
  


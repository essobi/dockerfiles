FROM bridg/java:oracle-jdk-8  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Dockerize  
ENV DOCKERIZE_VERSION=v0.2.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-
linux-amd64-${DOCKERIZE_VERSION}.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-
amd64-${DOCKERIZE_VERSION}.tar.gz \  
&& rm dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz  
  
# Install PrestoDB  
ENV PRESTO_VERSION=0.138 \  
PRESTO_CONFIG_DIR=/opt/presto-server/etc \  
PRESTO_DATA_DIR=/var/data/presto \  
PRESTO_DISCOVERY_URI= \  
PRESTO_DISCOVERY_SERVER_ENABLED=true \  
PRESTO_HOME=/opt/presto-server \  
PRESTO_HTTP_SERVER_PORT=8080 \  
PRESTO_IS_COORDINATOR=true \  
PRESTO_JVM_MEMORY= \  
PRESTO_LOG_LEVEL=INFO \  
PRESTO_MULTIPLE_TASKS_PER_NODE_ENABLED=true \  
PRESTO_NODE_ENVIRONMENT=default \  
PRESTO_NODE_SCHEDULER_INCLUDE_COORDINATOR=true \  
PRESTO_OPTIMIZER_USE_INTERMEDIATE_AGGREGATIONS=true \  
PRESTO_QUERY_MAX_MEMORY=1024GB \  
PRESTO_QUERY_MAX_MEMORY_PER_NODE=  
  
RUN wget "https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/${PRESTO_VERSION}/presto-server-${PRESTO_VERSION}.tar.gz" \  
-q -O - \  
| tar -xzv -C "/opt" \  
&& ln -s "/opt/presto-server-$PRESTO_VERSION" \  
"$PRESTO_HOME" \  
&& apt-get update \  
&& apt-get -y install python \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Directories and Volumes  
RUN mkdir -p "$PRESTO_CONFIG_DIR" "$PRESTO_DATA_DIR"  
VOLUME $PRESTO_CONFIG_DIR  
VOLUME $PRESTO_DATA_DIR  
  
# Add configure/run wrappers  
ADD templates/etc $PRESTO_HOME/etc  
ADD entrypoint.sh $PRESTO_HOME/entrypoint  
RUN chmod +x $PRESTO_HOME/entrypoint  
  
EXPOSE 8080  
ENV PATH $PRESTO_HOME:$PATH  
WORKDIR $PRESTO_HOME  
ENTRYPOINT ["entrypoint"]  


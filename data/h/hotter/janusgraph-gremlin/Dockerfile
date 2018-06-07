FROM openjdk:8u151-jdk  
LABEL maintainer "h-otter <h-otter@outlook.jp>"  
  
ENV JG_VERSION 0.2.0  
ENV DOCKERIZE_VERSION v0.6.0  
RUN curl -fsSLO
https://github.com/JanusGraph/janusgraph/releases/download/v${JG_VERSION}/janusgraph-${JG_VERSION}-hadoop2.zip
&& \  
unzip janusgraph-${JG_VERSION}-hadoop2.zip && \  
rm janusgraph-${JG_VERSION}-hadoop2.zip  
  
WORKDIR janusgraph-${JG_VERSION}-hadoop2  
COPY conf/gremlin-server/janusgraph-cassandra-es-server.properties
conf/gremlin-server/janusgraph-cassandra-es-server.properties  
COPY conf/gremlin-server/gremlin-server.yaml conf/gremlin-server/gremlin-
server.yaml  
RUN ["bin/gremlin-server.sh", "-i", "org.apache.tinkerpop", "gremlin-python",
"3.2.6"]  
  
RUN curl -fsSLO
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
EXPOSE 8182  
CMD ["bin/gremlin-server.sh"]  


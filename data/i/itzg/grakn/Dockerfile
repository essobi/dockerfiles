FROM openjdk:8-jre-alpine  
  
MAINTAINER itzg  
  
RUN apk -U add bash  
  
ENV GRAKN_VERSION=0.11.0  
ADD
https://github.com/graknlabs/grakn/releases/download/v${GRAKN_VERSION}/grakn-
dist-${GRAKN_VERSION}.tar.gz /tmp  
  
RUN mkdir -p /opt && \  
tar -C /opt -xvf /tmp/grakn-dist-${GRAKN_VERSION}.tar.gz && \  
rm -f /tmp/grakn-dist-${GRAKN_VERSION}.tar.gz  
  
EXPOSE 4567  
ENV KAFKA_SERVERS=kafka:9092 \  
CASSANDRA_HOST=cassandra \  
ZOOKEEPER_SERVESR=zookeeper:2181  
COPY grakn.in.sh /opt/grakn-dist-${GRAKN_VERSION}/bin  
COPY *.tmpl /conf/  
COPY start-grakn.sh /opt/  
  
ENTRYPOINT ["/opt/start-grakn.sh"]  
  
VOLUME ["/conf", "/logs"]  
  
WORKDIR /opt/grakn-dist-${GRAKN_VERSION}  


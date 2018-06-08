FROM anapsix/alpine-java:jdk8  
  
MAINTAINER Mansheng Yang  
  
RUN apk add --update wget jq coreutils  
  
ENV KAFKA_VERSION="0.10.0.0" SCALA_VERSION="2.11"  
ENV KAFKA_RELEASE_ARCHIVE kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
WORKDIR /tmp  
  
RUN wget
https://dist.apache.org/repos/dist/release/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}
&& \  
tar -xz -C /opt -f ${KAFKA_RELEASE_ARCHIVE} && \  
rm ${KAFKA_RELEASE_ARCHIVE}  
  
ENV KAFKA_HOME /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION}  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
  
VOLUME ["/data"]  
  
# Use "exec" form so that it runs as PID 1 (useful for graceful shutdown)  
CMD ["start-kafka.sh"]  


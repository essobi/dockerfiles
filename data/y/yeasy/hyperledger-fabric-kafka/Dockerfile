# Dockerfile for Hyperledger fabric kafka image.  
# This actually follows the official image.  
# github.com/yeasy/docker-hyperledger-fabric-kafka  
FROM anapsix/alpine-java:8  
LABEL maintainer "Baohua Yang <yeasy.github.com>"  
  
EXPOSE 9092  
EXPOSE 9093  
ENV SCALA_VERSION=2.11 \  
KAFKA_VERSION=0.10.2.0 \  
KAFKA_DOWNLOAD_SHA256=4c9e73059dea2dcb5022135f8e7eff5f187ffcc27a27b365b326ee61040214cd  
  
RUN apk update && apk add curl  
  
RUN curl -fSL "http://www-
us.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"
-o kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz \  
&& echo "${KAFKA_DOWNLOAD_SHA256} kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"
| sha256sum -c - \  
&& tar xfz kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt \  
&& mv /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION" /opt/kafka \  
&& rm kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz  
  
ADD payload/kafka-run-class.sh /opt/kafka/bin/kafka-run-class.sh  
ADD payload/docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/opt/kafka/bin/kafka-server-start.sh"]  
  
LABEL org.hyperledger.fabric.version=1.1.0 \  
org.hyperledger.fabric.base.version=0.4.2  


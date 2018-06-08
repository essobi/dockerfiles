FROM alpine:3.5  
LABEL \  
author="Przemyslaw Ozgo" \  
email="linux@ozgo.info" \  
description="Kafka in a docker"  
  
ENV \  
KAFKA_VERSION=0.10.2.0 \  
SCALA_VERSION=2.12 \  
KAFKA_HOME=/opt/kafka \  
PATH=${PATH}:${KAFKA_HOME}/bin  
  
ADD container-files /  
  
RUN \  
apk add --update bash openjdk8 wget docker && \  
wget -q -O /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz \  
ftp://ftp.mirrorservice.org/sites/ftp.apache.org/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
&& \  
mkdir -p /opt && \  
tar xfz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt && \  
rm /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz && \  
ln -s /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} /opt/kafka && \  
apk del wget && \  
rm -rf /var/cache/apk/*  
  
CMD ["start-kafka.sh"]  
  
EXPOSE 9092  


FROM anapsix/alpine-java  
MAINTAINER jang.jaehue@eland.co.kr  
  
RUN apk add --update unzip wget curl docker jq coreutils  
  
ENV KAFKA_VERSION="0.10.1.0" SCALA_VERSION="2.11"  
ADD download-kafka.sh /tmp/download-kafka.sh  
RUN chmod a+x /tmp/download-kafka.sh && /tmp/download-kafka.sh && tar xfz
/tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt && rm
/tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  


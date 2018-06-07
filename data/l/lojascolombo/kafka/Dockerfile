FROM java:openjdk-8-jdk-alpine  
MAINTAINER Lojas Colombo "projetos-site@colombo.com.br"  
ENV KAFKA_VERSION 0.10.0.1  
ENV SCALA_VERSION 2.11  
ENV KAFKA_RELEASE kafka_${SCALA_VERSION}-${KAFKA_VERSION}  
ENV KAFKA_URL_DOWNLOAD
https://archive.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE}.tgz  
  
RUN apk add --update bash unzip wget \  
&& wget -q "${KAFKA_URL_DOWNLOAD}" -O "/tmp/${KAFKA_RELEASE}.tgz" \  
&& tar xfz /tmp/${KAFKA_RELEASE}.tgz -C /tmp \  
&& mkdir -p /opt \  
&& mv /tmp/${KAFKA_RELEASE} /opt/kafka \  
&& rm /tmp/${KAFKA_RELEASE}.tgz \  
&& apk del unzip wget \  
&& rm -rf /var/cache/apk/*  
  
ADD start-kafka.sh /opt/kafka/bin/start-kafka.sh  
  
VOLUME /opt/kafka/logs  
WORKDIR /opt/kafka  
EXPOSE 2181 2888 3888  
CMD /opt/kafka/bin/start-kafka.sh  


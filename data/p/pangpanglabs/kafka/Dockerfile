FROM openjdk:8-jdk-alpine  
MAINTAINER pangpanglab <pangpanglab@p2shop.cn>  
  
ARG KAFKA_VERSION="1.1.0"  
ARG SCALA_VERSION="2.12"  
ENV KAFKA_HOME /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION}  
  
RUN mkdir /opt && \  
url="http://apache.mirror.cdnetworks.com/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"
&& \  
wget -q "${url}" -O "/tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz" && \  
tar xfz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt && \  
rm /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
RUN apk add --no-cache bash  
  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
ADD create-topics.sh /usr/bin/create-topics.sh  
  
RUN chmod a+x /usr/bin/start-kafka.sh && \  
chmod a+x /usr/bin/create-topics.sh  
  
CMD ["start-kafka.sh"]


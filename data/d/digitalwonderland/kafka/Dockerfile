# Apache Kafka  
FROM openjdk:8-jre-alpine  
  
ARG KAFKA_VERSION=0.10.2.1  
ARG KAFKA_MIRROR=http://www-eu.apache.org  
ARG KAFKA_SCALA_VERSION=2.12  
LABEL name="kafka" version=${KAFKA_VERSION}  
  
ENV KAFKA_HOME /opt/kafka  
  
ADD ./src /  
  
RUN chmod +x /usr/local/sbin/start.sh  
  
RUN apk add --no-cache wget bash  
  
RUN mkdir /opt \  
&& wget -q -O -
${KAFKA_MIRROR}/dist//kafka/${KAFKA_VERSION}/kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz
| tar -xzf - -C /opt \  
&& mv /opt/kafka_* $KAFKA_HOME \  
&& chown -R root:root $KAFKA_HOME  
  
RUN addgroup -S kafka \  
&& adduser -h /var/lib/kafka -G kafka -S -H -s /sbin/nologin kafka \  
&& mkdir /var/lib/kafka && chown -R kafka:kafka /var/lib/kafka \  
&& mkdir /var/log/kafka && chown -R kafka:kafka /var/log/kafka  
  
EXPOSE 9092  
VOLUME ["/var/lib/kafka", "/var/log/kafka"]  
  
ENTRYPOINT ["/usr/local/sbin/start.sh"]  


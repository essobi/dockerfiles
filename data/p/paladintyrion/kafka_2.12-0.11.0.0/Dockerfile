# Apache Kafka  
FROM openjdk:8-jre-alpine  
  
ARG KAFKA_VERSION=0.11.0.2  
ARG KAFKA_MIRROR=http://www-eu.apache.org  
ARG KAFKA_SCALA_VERSION=2.12  
LABEL name="kafka" version=${KAFKA_VERSION}  
  
ENV KAFKA_HOME /opt/kafka  
  
ENV KAFKA_HEAP_OPTS="-Xmx4G -Xms2G -XX:PermSize=64m -XX:MaxPermSize=128m"  
ENV JMX_PORT="9999"  
COPY ./src /  
  
RUN chmod +x /usr/local/sbin/start.sh  
  
RUN apk add --no-cache wget bash  
  
RUN mkdir /opt \  
&& wget -q -O -
${KAFKA_MIRROR}/dist/kafka/${KAFKA_VERSION}/kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz
| tar -xzf - -C /opt \  
&& mv /opt/kafka_* $KAFKA_HOME \  
&& chown -R root:root $KAFKA_HOME  
  
RUN addgroup -S kafka -g 440 \  
&& adduser -h /var/lib/kafka -G kafka -u 440 -S -H -s /sbin/nologin kafka \  
&& mkdir -p /var/lib/kafka && chown -R kafka:kafka /var/lib/kafka \  
&& mkdir -p /var/log/kafka && chown -R kafka:kafka /var/log/kafka  
  
EXPOSE 9092 9999  
VOLUME ["/var/lib/kafka", "/var/log/kafka"]  
  
ENTRYPOINT ["/usr/local/sbin/start.sh"]  


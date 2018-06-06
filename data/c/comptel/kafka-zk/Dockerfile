FROM openjdk:8-jdk-alpine  
  
ARG SCALA_VERSION=2.12  
ARG KAFKA_VERSION=1.0.1  
ARG ZOOKEEPER_VERSION=3.4.11  
ARG DUMB_INIT_VERSION=1.2.1  
ENV KAFKA_HOME /opt/kafka  
ENV ZOOKEEPER_HOME /opt/zookeeper  
ENV PATH $PATH:$KAFKA_HOME/bin:$ZOOKEEPER_HOME/bin  
  
COPY start-kafka.sh /start-kafka.sh  
  
WORKDIR /tmp  
  
# Dependencies + dumb-init  
RUN apk add --no-cache ca-certificates openssl curl bash jq && \  
wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 && \  
chmod +x /usr/bin/dumb-init && \  
mkdir -p ${KAFKA_HOME} ${ZOOKEEPER_HOME} && \  
addgroup fwdkafka && adduser -s /bin/bash -D -G fwdkafka fwdkafka && \  
wget -q -O - $(wget -q -O - "http://www.apache.org/dyn/closer.cgi?as_json=1" |
jq -r
.preferred)/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
| \  
tar -xzf - -C /tmp && \  
mv /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}/* ${KAFKA_HOME} && \  
rm -rf /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION} && \  
wget -q -O - $(wget -q -O - "http://www.apache.org/dyn/closer.cgi?as_json=1" |
jq -r
.preferred)/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz
| \  
tar -xzf - -C /tmp && \  
mv /tmp/zookeeper-${ZOOKEEPER_VERSION}/* ${ZOOKEEPER_HOME} && \  
rm -rf /tmp/zookeeper-${ZOOKEEPER_VERSION} && \  
cp ${ZOOKEEPER_HOME}/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg && \  
chown -R fwdkafka:fwdkafka /opt ${KAFKA_HOME} ${ZOOKEEPER_HOME} /start-
kafka.sh && \  
chown -R fwdkafka:fwdkafka ${ZOOKEEPER_HOME} /start-kafka.sh && \  
apk del openssl && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /opt  
  
USER fwdkafka  
  
ENTRYPOINT ["/usr/bin/dumb-init"]  
  
# zookeeper and kafka  
EXPOSE 2181 9092  
CMD ["/start-kafka.sh"]  


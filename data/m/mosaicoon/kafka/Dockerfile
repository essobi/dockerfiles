FROM mosaicoon/java-8-alpine-bash  
  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.9.0.1  
ENV SOFTWARE_DIR kafka  
  
ENV ZOOKEEPER_HOST zookeeper  
ENV ZOOKEEPER_PORT 2181  
ENV ADVERTISED_HOST_NAME localhost  
ENV BROKER_ID -1  
ENV BROKER_ID_GENERATION_ENABLE true  
ENV AUTO_CREATE_TOPICS_ENABLE true  
ENV BACKGROUND_THREADS 10  
ENV NUM_IO_THREAD 8  
ENV NUM_NETWORK_THREADS 3  
ENV DELETE_TOPIC_ENABLE true  
ENV PORT 9092  
# RMI_PORT must be JMX_PORT + 1  
ENV RMI_PORT 10000  
ENV JMX_PORT 9999  
ENV KAFKA_HEAP_OPTS -Xmx2048m -Xms512m  
ENV _JAVA_OPTIONS="-Djava.net.preferIPv4Stack=true"  
WORKDIR /usr/src/"${SOFTWARE_DIR}"/  
  
RUN apk add --update wget && \  
wget --no-check-certificate
http://mirrors.muzzy.it/apache/kafka/"${KAFKA_VERSION}"/kafka_"${SCALA_VERSION}"-"${KAFKA_VERSION}".tgz
&& \  
apk del wget && \  
/bin/tar -zxvf kafka_"${SCALA_VERSION}"-"${KAFKA_VERSION}".tgz && \  
rm -f kafka_"${SCALA_VERSION}"-"${KAFKA_VERSION}".tgz && \  
rm -rf /var/cache/apk/*  
  
WORKDIR
/usr/src/"${SOFTWARE_DIR}"/kafka_"${SCALA_VERSION}"-"${KAFKA_VERSION}"/  
  
EXPOSE ${PORT} ${JMX_PORT} ${RMI_PORT}  
  
CMD ./bin/kafka-server-start.sh ./config/server.properties --override
zookeeper.connect=${ZOOKEEPER_HOST}:${ZOOKEEPER_PORT} \--override
advertised.host.name=${ADVERTISED_HOST_NAME} \--override
broker.id=${BROKER_ID} \--override
broker.id.generation.enable=${BROKER_ID_GENERATION_ENABLE} \--override
auto.create.topics.enable=${AUTO_CREATE_TOPICS_ENABLE} \--override
background.threads=${BACKGROUND_THREADS} \--override
num.io.thread=${NUM_IO_THREAD} \--override
num.network.threads=${NUM_NETWORK_THREADS} \--override
delete.topic.enable=${DELETE_TOPIC_ENABLE} \--override port=${PORT}


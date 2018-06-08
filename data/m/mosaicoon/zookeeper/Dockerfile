FROM mosaicoon/java-8-alpine-bash  
  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.9.0.1  
ENV SOFTWARE_DIR zookeeper  
  
WORKDIR /usr/src/"${SOFTWARE_DIR}"/  
  
RUN apk add --update wget && \  
wget --no-check-certificate
http://mirrors.muzzy.it/apache/kafka/"${KAFKA_VERSION}"/kafka_"${SCALA_VERSION}"-"${KAFKA_VERSION}".tgz
&& \  
apk del wget && \  
/bin/tar -zxvf kafka_"${SCALA_VERSION}"-"${KAFKA_VERSION}".tgz && \  
rm -f kafka_"${SCALA_VERSION}"-"${KAFKA_VERSION}".tgz  
  
WORKDIR
/usr/src/"${SOFTWARE_DIR}"/kafka_"${SCALA_VERSION}"-"${KAFKA_VERSION}"/  
  
EXPOSE 2181  
CMD ["./bin/zookeeper-server-start.sh", "./config/zookeeper.properties"]


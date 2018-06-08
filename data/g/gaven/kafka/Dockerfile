FROM gaven/alpine:8-jre  
  
MAINTAINER gavin-guo  
  
RUN apk add --no-cache \  
bash \  
supervisor \  
snappy  
  
ENV SCALA_VERSION=2.11 \  
KAFKA_VERSION=1.0.0 \  
ZOOKEEPER_VERSION=3.4.10 \  
KAFDROP_VERSION=2.0.0  
ENV KAFKA_HOME="/kafka" \  
ZOOKEEPER_HOME="/zookeeper"  
RUN set -x \  
&& apk update \  
&& apk add --no-cache --virtual .build-deps \  
ca-certificates \  
wget \  
tar \  
&& wget -q
"http://www.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz"
\  
&& tar -xzf "zookeeper-${ZOOKEEPER_VERSION}.tar.gz" \  
&& mv "zookeeper-${ZOOKEEPER_VERSION}" "$ZOOKEEPER_HOME" \  
&& cp "$ZOOKEEPER_HOME/conf/zoo_sample.cfg" "$ZOOKEEPER_HOME/conf/zoo.cfg" \  
&& wget -q
"http://mirror.reverse.net/pub/apache/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"
\  
&& tar -xzf "kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz" \  
&& mv "kafka_${SCALA_VERSION}-${KAFKA_VERSION}" "$KAFKA_HOME" \  
&& wget -q
"http://sftp.chinacloudapp.cn/docker/kafdrop-${KAFDROP_VERSION}.jar" -O
/kafdrop.jar \  
&& rm -r "zookeeper-${ZOOKEEPER_VERSION}.tar.gz"
"kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz" \  
&& apk del .build-deps  
  
RUN set -x \  
&& mkdir /log /config /scripts  
  
COPY supervisord.conf /config/  
COPY scripts/* /scripts/  
COPY docker-entrypoint.sh /scripts/  
  
RUN set -x \  
&& chmod +x /scripts/*  
  
ENV PATH=$PATH:${ZOOKEEPER_HOME}/bin:$KAFKA_HOME/bin:/scripts  
  
WORKDIR $KAFKA_HOME/bin  
  
EXPOSE 2181 9092 9000  
ENTRYPOINT ["/scripts/docker-entrypoint.sh"]


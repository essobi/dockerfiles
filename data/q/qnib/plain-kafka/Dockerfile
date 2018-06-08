ARG DOCKER_REGISTRY=docker.io  
ARG DOCKER_IMG_TAG=":2018-04-25_0.3.0"  
ARG
DOCKER_IMG_HASH="@sha256:bac2b14174d7908eb94f6b4d247ff765d0488397227a8a17e3ebeac6ce3d5d18"  
FROM ${DOCKER_REGISTRY}/qnib/alplain-
openjre8-prometheus${DOCKER_IMG_TAG}${DOCKER_IMG_HASH}  
  
ARG KAFKA_VER=1.1.0  
ARG API_VER=2.12  
LABEL kafka.version=${API_VER}-${KAFKA_VER}  
ENV KAFKA_PORT=9092 \  
PROMETHEUS_JMX_PROFILE=kafka \  
PROMETHEUS_JMX_ENABLE=false \  
ENTRYPOINTS_DIR=/opt/qnib/entry \  
ZK_SERVERS=tasks.zookeeper \  
INTER_BROKER_PROTOCOL_VERSION=1.0 \  
LOG_MESSAGE_FORMAT_VERSION=1.0 \  
KAFKA_ID_OFFSET=0  
RUN apk --no-cache add curl bc \  
&& mkdir -p /opt/kafka \  
&& curl -fLs
http://apache.mirrors.pair.com/kafka/${KAFKA_VER}/kafka_${API_VER}-${KAFKA_VER}.tgz
|tar xzf - --strip-component=1 -C /opt/kafka \  
&& apk --no-cache del curl  
COPY opt/qnib/entry/*.sh /opt/qnib/entry/  
COPY opt/qnib/kafka/bin/start.sh /opt/qnib/kafka/bin/  
COPY opt/qnib/kafka/conf/server.properties /opt/qnib/kafka/conf/  
COPY opt/prometheus/jmx/kafka.yml /opt/prometheus/jmx/  
HEALTHCHECK \--interval=2s --retries=15 --timeout=1s \  
CMD netstat -plnt |grep 9092  
CMD ["/opt/qnib/kafka/bin/start.sh"]  


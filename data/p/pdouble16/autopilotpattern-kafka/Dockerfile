FROM pdouble16/autopilotpattern-base:1.2.0  
FROM pdouble16/kafkacat:1.3.1-r1  
FROM wurstmeister/kafka:1.1.0  
ARG SOURCE_REF  
ARG SOURCE_TYPE  
ARG DOCKERFILE_PATH  
ARG BUILD_DATE  
  
# libcrypto1.0 libssl1.0 is required for kafkacat  
RUN apk add --no-cache nginx jq curl libcrypto1.0 libssl1.0 &&\  
rm -rf /tmp/* /var/cache/apk/* &&\  
mkdir /opt/prometheus &&\  
wget -O /opt/prometheus/jmx_prometheus_javaagent.jar
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.1.0/jmx_prometheus_javaagent-0.1.0.jar
&&\  
wget -O /opt/prometheus/jmx_prometheus_httpserver-jar-with-dependencies.jar
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_httpserver/0.1.0/jmx_prometheus_httpserver-0.1.0-jar-
with-dependencies.jar &&\  
mkdir /run/nginx /var/lib/nginx/cache  
  
RUN mkdir -p /var/lib/consul /etc/consul  
COPY \--from=0 /usr/local/bin/* /usr/local/bin/  
COPY \--from=0 /etc/consul/* /etc/consul/  
COPY \--from=1 /usr/local/bin/kafkacat /usr/bin/kafkacat  
  
# Fixes for incorrect parsing of environment  
ADD https://raw.githubusercontent.com/wurstmeister/kafka-
docker/fcef1c929e0db173fc9e5b1d8f01597d17e9f103/start-kafka.sh /usr/bin/start-
kafka.sh  
RUN chmod +x /usr/bin/start-kafka.sh  
# Fix for create-topics.sh to wait for enough brokers  
COPY opt/kafka/bin/create-topics.sh /usr/bin/create-topics.sh  
  
ENV _JAVA_OPTIONS="-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap" \  
KAFKA_JMX_OPTS="-Dcom.sun.management.jmxremote
-Dcom.sun.management.jmxremote.authenticate=false
-Dcom.sun.management.jmxremote.ssl=false
-Dcom.sun.management.jmxremote.rmi.port=5000" \  
JMX_PORT="5000" \  
HOSTNAME_COMMAND="/opt/kafka/bin/kafka-manage hostname" \  
PORT_COMMAND="/opt/kafka/bin/kafka-manage outsideport" \  
RACK_COMMAND="/opt/kafka/bin/kafka-manage rack" \  
KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \  
KAFKA_ADVERTISED_LISTENERS=INSIDE://:9092,OUTSIDE://_{HOSTNAME_COMMAND}:_{PORT_COMMAND},BROKER://:9093
\  
KAFKA_LISTENERS=INSIDE://:9092,OUTSIDE://:9094,BROKER://:9093 \  
KAFKA_LISTENER_SECURITY_PROTOCOL_MAP="INSIDE:PLAINTEXT,OUTSIDE:SSL,BROKER:PLAINTEXT"
\  
KAFKA_INTER_BROKER_LISTENER_NAME=BROKER \  
KAFKA_INTER_BROKER_PORT=9093 \  
CONTAINERPILOT="/etc/containerpilot.json5"  
COPY nginx.conf /etc/nginx/  
  
COPY kafka-prometheus.yml /opt/prometheus/  
COPY opt/kafka/bin/* /opt/kafka/bin/  
  
COPY etc/containerpilot.json5 ${CONTAINERPILOT}  
  
CMD ["/usr/local/bin/containerpilot"]  
  
EXPOSE 9092 9093 9094 9090 5000 8301 8301/udp 8302 8302/udp  
HEALTHCHECK \--interval=120s --timeout=10s --retries=3 CMD /usr/bin/test
"$(cat /var/run/kafka-healthcheck)" = "0" || exit 1  
  
LABEL maintainer="Patrick Double (pat@patdouble.com)" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="MPL-2.0" \  
org.label-schema.vendor="https://bitbucket.org/double16" \  
org.label-schema.name="Autopilot Pattern for Kafka Broker with full Prometheus
Telemetry" \  
org.label-schema.url="https://bitbucket.org/double16/autopilotpattern-kafka" \  
org.label-schema.docker.dockerfile="${DOCKERFILE_PATH}/Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type=$SOURCE_TYPE \  
org.label-schema.vcs-url="https://bitbucket.org/double16/autopilotpattern-
kafka.git"  


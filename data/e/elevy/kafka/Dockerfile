FROM elevy/slim_java:8  
  
ENV KAFKA_VERSION=0.11.0.1 \  
SCALA_VERSION=2.11  
ENV KAFKA_RELEASE ${SCALA_VERSION}-${KAFKA_VERSION}  
  
RUN apk add \--no-cache \--virtual .build-deps \  
ca-certificates \  
gnupg \  
tar \  
wget && \  
#  
# Install dependencies  
apk add \--no-cache \  
bash && \  
#  
# Download Kafka  
wget -nv -O /tmp/kafka.tgz
"https://www.apache.org/dyn/closer.cgi?action=download&filename=kafka/${KAFKA_VERSION}/kafka_${KAFKA_RELEASE}.tgz"
&& \  
wget -nv -O /tmp/kafka.tgz.asc
"https://dist.apache.org/repos/dist/release/kafka/${KAFKA_VERSION}/kafka_${KAFKA_RELEASE}.tgz.asc"
&& \  
wget -nv -O /tmp/KEYS https://kafka.apache.org/KEYS && \  
#  
# Verify the signature  
export GNUPGHOME="$(mktemp -d)" && \  
gpg -q \--batch \--import /tmp/KEYS && \  
gpg -q \--batch \--no-auto-key-retrieve \--verify /tmp/kafka.tgz.asc
/tmp/kafka.tgz && \  
#  
# Set up directories  
#  
mkdir -p /kafka/{config,data,logs,templates} && \  
#  
# Install  
tar -x -C /kafka \--strip-components=1 \--no-same-owner -f /tmp/kafka.tgz
\--wildcards '*/bin/*.sh' '*/libs/' && \  
#  
# Slim down  
cd /kafka && \  
rm -rf \  
bin/zookeeper-server-*.sh \  
libs/*-javadoc.jar \  
libs/*-scaladoc.jar \  
libs/*-sources.jar \  
libs/*-test.jar \  
libs/*.asc \  
libs/kafka-streams-examples-*.jar && \  
#  
# Clean up  
apk del .build-deps && \  
rm -rf /tmp/* "$GNUPGHOME"  
  
COPY config /kafka/config/  
COPY entrypoint.sh /  
  
ENV PATH="/kafka/bin:$PATH" \  
JMX_PORT=7203 \  
KAFKA_JVM_PERFORMANCE_OPTS="-XX:MetaspaceSize=48m -XX:MaxMetaspaceSize=48m
-XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35
-XX:+DisableExplicitGC"  
#USER kafka  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
  
CMD [ "kafka-server-start.sh", "/kafka/config/server.properties" ]  
  
# Kafka, JMX  
EXPOSE 9092 7203  


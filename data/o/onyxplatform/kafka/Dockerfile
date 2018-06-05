FROM solsson/kafka-
jre@sha256:7765513cf5fa455a672a06f584058c1c81cc0b3b56cc56b0cfdf1a917a183f26  
## Attribution: https://github.com/solsson/dockerfiles/tree/master/kafka  
ENV KAFKA_VERSION=0.11.0.1 SCALA_VERSION=2.11  
ENV kafka_bin_version=2.11-$kafka_version  
  
  
RUN set -ex; \  
export DEBIAN_FRONTEND=noninteractive; \  
runDeps='netcat-openbsd'; \  
buildDeps='curl ca-certificates'; \  
apt-get update && apt-get install -y $runDeps $buildDeps \--no-install-
recommends; \  
\  
SCALA_BINARY_VERSION=$(echo $SCALA_VERSION | cut -f 1-2 -d '.'); \  
mkdir -p /opt/kafka; \  
curl -SLs "https://www-
eu.apache.org/dist/kafka/$KAFKA_VERSION/kafka_$SCALA_BINARY_VERSION-$KAFKA_VERSION.tgz"
| tar -xzf - --strip-components=1 -C /opt/kafka; \  
\  
rm -rf /opt/kafka/site-docs; \  
\  
apt-get purge -y --auto-remove $buildDeps; \  
rm -rf /var/lib/apt/lists/*; \  
rm -rf /var/log/dpkg.log /var/log/alternatives.log /var/log/apt  
  
WORKDIR /opt/kafka  
ENTRYPOINT ["bin/kafka-server-start.sh"]  
  
ADD
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.9/jmx_prometheus_javaagent-0.9.jar
/opt/kafka/jmx_prometheus_javaagent.jar  
ADD container-limits kfRunServer.sh /opt/kafka/  
  
RUN sed -i
's/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper:2181/'
config/server.properties  
CMD ["config/server.properties"]  


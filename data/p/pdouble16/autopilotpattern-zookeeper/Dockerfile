FROM pdouble16/autopilotpattern-base:1.2.0  
FROM openjdk:8u151-jre-alpine  
  
ARG BUILD_DATE  
ARG SOURCE_TYPE  
ARG SOURCE_REF  
ARG DOCKERFILE_PATH  
  
RUN mkdir -p /var/lib/consul /etc/consul  
COPY \--from=0 /usr/local/bin/* /usr/local/bin/  
COPY \--from=0 /etc/consul/* /etc/consul/  
  
ENV _JAVA_OPTIONS="-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap" \  
JMXLOCALONLY="true" \  
JMXPORT="5000" \  
ZOOKEEPER_VERSION="3.4.12" \  
ZK_HOME="/opt/zookeeper-3.4.12" \  
CONTAINERPILOT="/etc/containerpilot.json5"  
# Zookeeper from https://github.com/wurstmeister/zookeeper-
docker/blob/master/Dockerfile  
# bash is required for zookeeper scripts  
RUN apk --no-cache add nginx gnupg curl wget bash jq && \  
#Download Zookeeper  
wget -q
http://www.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz
&& \  
wget -q https://www.apache.org/dist/zookeeper/KEYS && \  
wget -q
https://www.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz.asc
&& \  
wget -q
https://www.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz.md5
&& \  
#Verify download  
md5sum -c zookeeper-${ZOOKEEPER_VERSION}.tar.gz.md5 && \  
gpg --import KEYS && \  
gpg --verify zookeeper-${ZOOKEEPER_VERSION}.tar.gz.asc && \  
#Install  
mkdir /opt && tar -xzf zookeeper-${ZOOKEEPER_VERSION}.tar.gz -C /opt && \  
rm zookeeper-${ZOOKEEPER_VERSION}.tar.gz.md5
zookeeper-${ZOOKEEPER_VERSION}.tar.gz.asc
zookeeper-${ZOOKEEPER_VERSION}.tar.gz KEYS && \  
#Configure  
mv /opt/zookeeper-${ZOOKEEPER_VERSION}/conf/zoo_sample.cfg
/opt/zookeeper-${ZOOKEEPER_VERSION}/conf/zoo.cfg && \  
sed -i "s|/tmp/zookeeper|$ZK_HOME/data|g" $ZK_HOME/conf/zoo.cfg; mkdir
$ZK_HOME/data \  
# Prometheus  
&& mkdir /opt/prometheus &&\  
wget -O /opt/prometheus/jmx_prometheus_javaagent.jar
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.1.0/jmx_prometheus_javaagent-0.1.0.jar
\  
&& wget -O /opt/prometheus/jmx_prometheus_httpserver-jar-with-dependencies.jar
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_httpserver/0.1.0/jmx_prometheus_httpserver-0.1.0-jar-
with-dependencies.jar \  
&& mkdir /run/nginx /var/lib/nginx/cache \  
&& apk del gnupg  
  
COPY nginx.conf /etc/nginx/  
COPY zookeeper-prometheus.yml /opt/prometheus/zookeeper-prometheus.yml  
COPY bin/health /usr/local/bin/  
COPY etc/containerpilot.json5 ${CONTAINERPILOT}  
ADD start-zk.sh /usr/bin/start-zk.sh  
  
WORKDIR /opt/zookeeper-${ZOOKEEPER_VERSION}  
VOLUME ["/opt/zookeeper-${ZOOKEEPER_VERSION}/conf",
"/opt/zookeeper-${ZOOKEEPER_VERSION}/data"]  
CMD ["/usr/local/bin/containerpilot"]  
EXPOSE 2181 2888 3888 9090 9100 8301 8301/udp 8302 8302/udp  
HEALTHCHECK \--interval=120s --timeout=30s --retries=2 CMD /usr/bin/test
"$(cat /var/run/zookeeper-healthcheck)" = "0" || exit 1  
  
LABEL maintainer='Patrick Double "pat@patdouble.com"' \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="MPL-2.0" \  
org.label-schema.vendor="https://bitbucket.org/double16" \  
org.label-schema.name="Zookeeper with Prometheus Telemetry" \  
org.label-schema.url="https://bitbucket.org/double16/autopilotpattern-
zookeeper" \  
org.label-schema.docker.dockerfile="Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type='git' \  
org.label-schema.vcs-url="https://bitbucket.org/double16/autopilotpattern-
zookeeper.git"  


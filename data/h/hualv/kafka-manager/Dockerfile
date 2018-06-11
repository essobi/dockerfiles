FROM openjdk:8-jdk-alpine  
MAINTAINER laoshancun@foxmail.com  
  
ENV SBT_VERSION="0.13.15" \  
SBT_HOME=/usr/local/sbt-launcher-packaging-${SBT_VERSION} \  
PATH="${PATH}:${SBT_HOME}/bin" \  
KAFKA_MANAGER_VERSION="1.3.3.16" \  
KAFKA_MANAGER_HOME=/opt/kafka-manager \  
ZK_HOSTS="localhost:2181" \  
KAFKA_MANAGER_CONFIGFILE="conf/application.conf"  
  
ADD repositories /etc/apk/repositories  
ADD start-kafka-manager.sh /opt/kafka-manager-${KAFKA_MANAGER_VERSION}/  
RUN set -ex \  
&& apk add --no-cache --virtual /tmp/.build-deps \  
unzip \  
curl \  
gzip \  
tar \  
bash \  
# Install sbt  
&& curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local \  
&& echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built \  
# Install kafka-manager  
&& mkdir -p /tmp \  
&& cd /tmp \  
&& curl -sL -o kafka-manager-${KAFKA_MANAGER_VERSION}.zip
https://github.com/yahoo/kafka-manager/archive/${KAFKA_MANAGER_VERSION}.zip \  
&& unzip -d /tmp/kafka-manager kafka-manager-${KAFKA_MANAGER_VERSION}.zip \  
&& cd /tmp/kafka-manager/kafka-manager-${KAFKA_MANAGER_VERSION} \  
&& ./sbt clean dist \  
&& unzip -d /opt ./target/universal/kafka-manager-${KAFKA_MANAGER_VERSION}.zip
\  
&& chmod +x /opt/kafka-manager-${KAFKA_MANAGER_VERSION}/start-kafka-manager.sh
\  
# clean up  
#&& apk del /tmp/.build-deps \  
&& rm -fr /tmp/* /root/.sbt /root/.built /root/.ivy2  
  
  
WORKDIR /opt/kafka-manager-${KAFKA_MANAGER_VERSION}/  
EXPOSE 9000  
CMD ["./start-kafka-manager.sh"]  


FROM openjdk:8-jdk-alpine  
MAINTAINER Francis Chuang <francis.chuang@boostport.com>  
  
ENV EXHIBITOR_VER 1.5.6  
ENV ZOOKEEPER_VER 3.4.9  
  
RUN apk --no-cache --update add bash ca-certificates gnupg openssl su-exec tar
\  
&& apk --no-cache --update --repository
https://dl-3.alpinelinux.org/alpine/edge/community/ add maven \  
&& update-ca-certificates \  
\  
# Set up directories  
&& mkdir -p /opt/zookeeper \  
&& mkdir -p /opt/exhibitor \  
&& mkdir -p /var/lib/zookeeper/data \  
\  
# Download Zookeeper  
&& wget -O /tmp/KEYS https://apache.org/dist/zookeeper/KEYS \  
&& gpg --import /tmp/KEYS \  
&& wget -q -O /tmp/zookeeper.tar.gz
http://apache.mirror.serversaustralia.com.au/zookeeper/zookeeper-${ZOOKEEPER_VER}/zookeeper-${ZOOKEEPER_VER}.tar.gz
\  
&& wget -O /tmp/zookeeper.asc
https://apache.org/dist/zookeeper/zookeeper-$ZOOKEEPER_VER/zookeeper-$ZOOKEEPER_VER.tar.gz.asc
\  
&& gpg --verify /tmp/zookeeper.asc /tmp/zookeeper.tar.gz \  
&& tar -xzf /tmp/zookeeper.tar.gz -C /opt/zookeeper --strip-components 1 \  
\  
# Build exhibitor  
&& mkdir -p /tmp/exhibitor \  
&& wget -O /tmp/exhibitor/pom.xml
https://raw.githubusercontent.com/soabase/exhibitor/v${EXHIBITOR_VER}/exhibitor-
standalone/src/main/resources/buildscripts/standalone/maven/pom.xml \  
&& cd /tmp/exhibitor \  
&& mvn clean package \  
&& mv /tmp/exhibitor/target/exhibitor-1.5.5.jar /opt/exhibitor/exhibitor.jar \  
\  
# Set up permissions  
&& addgroup -S zookeeper \  
&& adduser -h /opt/zookeeper -G zookeeper -S -D -H -s /bin/false -g zookeeper
zookeeper \  
&& chown -R zookeeper:zookeeper /opt/zookeeper \  
&& chown -R zookeeper:zookeeper /opt/exhibitor \  
&& chown -R zookeeper:zookeeper /var/lib/zookeeper/data \  
\  
# Clean up  
&& apk del gnupg maven openssl tar \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/*  
  
ADD run-exhibitor.sh /run-exhibitor.sh  
  
VOLUME ["/var/lib/zookeeper/data"]  
  
EXPOSE 2181 2888 3888 8080  
  
CMD ["/run-exhibitor.sh"]


FROM openjdk:8-jre-alpine  
MAINTAINER Francis Chuang <francis.chuang@boostport.com>  
  
ENV HBASE_MINOR_VERSION 1.3  
ENV PHOENIX_VERSION 4.13.1  
  
RUN apk \--no-cache \--update add bash ca-certificates gnupg openssl python
su-exec tar \  
&& apk \--no-cache \--update \--repository
https://dl-3.alpinelinux.org/alpine/edge/community/ add xmlstarlet \  
&& update-ca-certificates \  
\  
# Set up directories  
&& mkdir -p /opt/phoenix-server \  
&& mkdir -p /tmp/phoenix \  
\  
# Download phoenix  
&& wget -O /tmp/KEYS https://www-us.apache.org/dist/phoenix/KEYS \  
&& gpg \--import /tmp/KEYS \  
&& wget -q -O /tmp/phoenix.tar.gz
http://apache.uberglobalmirror.com/phoenix/apache-phoenix-$PHOENIX_VERSION-
HBase-$HBASE_MINOR_VERSION/bin/apache-phoenix-$PHOENIX_VERSION-
HBase-$HBASE_MINOR_VERSION-bin.tar.gz \  
&& wget -O /tmp/phoenix.asc https://www-eu.apache.org/dist/phoenix/apache-
phoenix-$PHOENIX_VERSION-HBase-$HBASE_MINOR_VERSION/bin/apache-
phoenix-$PHOENIX_VERSION-HBase-$HBASE_MINOR_VERSION-bin.tar.gz.asc \  
&& gpg \--verify /tmp/phoenix.asc /tmp/phoenix.tar.gz \  
&& tar -xzf /tmp/phoenix.tar.gz -C /tmp/phoenix \--strip-components 1 \  
\  
# Set up phoenix server  
&& mv /tmp/phoenix/phoenix-$PHOENIX_VERSION-HBase-$HBASE_MINOR_VERSION-
queryserver.jar /opt/phoenix-server/ \  
&& mv /tmp/phoenix/phoenix-$PHOENIX_VERSION-HBase-$HBASE_MINOR_VERSION-
client.jar /opt/phoenix-server/ \  
&& mv /tmp/phoenix/bin /opt/phoenix-server/bin \  
\  
# Set up permissions  
&& addgroup -S phoenix-server \  
&& adduser -h /opt/phoenix-server -G phoenix-server -S -D -H -s /bin/false -g
phoenix-server phoenix-server \  
&& chown -R phoenix-server:phoenix-server /opt/phoenix-server \  
\  
# Clean up  
&& apk del gnupg openssl tar \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/*  
  
ADD run-phoenix-server.sh /run-phoenix-server.sh  
  
EXPOSE 8765  
  
CMD ["/run-phoenix-server.sh"]


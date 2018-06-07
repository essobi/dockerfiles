FROM openjdk:alpine  
  
ARG FLUME_VERSION="1.6.0"  
ARG HADOOP_VERSION="2.7.3"  
ARG APACHE_MIRROR="https://dist.apache.org/repos/dist/release"  
ARG APACHE_DIST_MIRROR="https://dist.apache.org/repos/dist/release"  
RUN set -x \  
&& apk add --no-cache gettext bash gnupg ca-certificates openssl \  
&& update-ca-certificates \  
&& wget -q -P /tmp
"${APACHE_MIRROR}/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz"
\  
&& wget -q -P /tmp
"${APACHE_DIST_MIRROR}/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz.asc"
\  
&& wget -q -O /tmp/hadoop-KEYS "${APACHE_DIST_MIRROR}/hadoop/common/KEYS" \  
&& gpg --import /tmp/hadoop-KEYS \  
&& gpg --verify /tmp/hadoop-${HADOOP_VERSION}.tar.gz.asc \  
&& tar xzf /tmp/hadoop-${HADOOP_VERSION}.tar.gz -C /tmp \  
&& mv /tmp/hadoop-${HADOOP_VERSION}/ /hadoop \  
&& wget -q -P /tmp "${APACHE_MIRROR}/flume/${FLUME_VERSION}/apache-
flume-${FLUME_VERSION}-bin.tar.gz" \  
&& wget -q -P /tmp "${APACHE_DIST_MIRROR}/flume/${FLUME_VERSION}/apache-
flume-${FLUME_VERSION}-bin.tar.gz.asc" \  
&& wget -q -O /tmp/apache-flume-KEYS "${APACHE_DIST_MIRROR}/flume/KEYS" \  
&& gpg --import /tmp/apache-flume-KEYS \  
&& gpg --verify /tmp/apache-flume-${FLUME_VERSION}-bin.tar.gz.asc \  
&& tar xzf /tmp/apache-flume-${FLUME_VERSION}-bin.tar.gz -C /tmp \  
&& mv /tmp/apache-flume-${FLUME_VERSION}-bin /flume \  
&& cp /flume/conf/flume-conf.properties.template /flume/conf/flume.properties
\  
&& rm -rf /tmp/*  
  
ENV HADOOP_HOME=/hadoop  
EXPOSE 41414  
WORKDIR /flume  
# Expose flume config dir as a volume  
VOLUME /flume/conf  
  
# Entrypoint  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  


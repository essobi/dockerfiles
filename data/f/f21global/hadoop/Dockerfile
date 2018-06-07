FROM openjdk:8-jdk-alpine  
MAINTAINER Francis Chuang <francis.chuang@boostport.com>  
  
ENV HADOOP_VER=2.8.2 HADOOP_PREFIX=/opt/hadoop  
  
RUN apk --no-cache --update add bash ca-certificates gnupg openssl su-exec tar
\  
&& apk --no-cache --update --repository
https://dl-3.alpinelinux.org/alpine/edge/community/ add xmlstarlet \  
&& update-ca-certificates \  
\  
# Set up directories  
&& mkdir -p $HADOOP_PREFIX \  
&& mkdir -p /var/lib/hadoop \  
\  
# Download Hadoop  
&& wget -O /tmp/KEYS
https://dist.apache.org/repos/dist/release/hadoop/common/KEYS \  
&& gpg --import /tmp/KEYS \  
&& wget -q -O /tmp/hadoop.tar.gz
http://apache.mirror.digitalpacific.com.au/hadoop/common/hadoop-$HADOOP_VER/hadoop-$HADOOP_VER.tar.gz
\  
&& wget -O /tmp/hadoop.asc
https://dist.apache.org/repos/dist/release/hadoop/common/hadoop-$HADOOP_VER/hadoop-$HADOOP_VER.tar.gz.asc
\  
&& gpg --verify /tmp/hadoop.asc /tmp/hadoop.tar.gz \  
&& tar -xzf /tmp/hadoop.tar.gz -C $HADOOP_PREFIX --strip-components 1 \  
\  
# Set up permissions  
&& addgroup -S hadoop \  
&& adduser -h $HADOOP_PREFIX -G hadoop -S -D -H -s /bin/false -g hadoop hadoop
\  
&& chown -R hadoop:hadoop $HADOOP_PREFIX \  
&& chown -R hadoop:hadoop /var/lib/hadoop \  
\  
# Clean up  
&& apk del gnupg openssl tar \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/*  
  
VOLUME ["/var/lib/hadoop"]  
  
ADD ["run-hadoop.sh", "/"]  
ADD ["/roles", "/roles"]  
  
# Namenode Datanode Journalnode  
EXPOSE 8020 9000 50070 50470 50010 50075 50475 1006 50020 8485 8480 8481  
  
CMD ["/run-hadoop.sh"]


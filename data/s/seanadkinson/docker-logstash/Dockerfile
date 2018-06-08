FROM million12/centos-supervisor  
MAINTAINER Przemyslaw Ozgo <linux@ozgo.info>  
  
ADD env.sh /config/init/env.sh  
ADD certs.sh /config/init/certs.sh  
ADD logstash.conf /etc/logstash.d/logstash.conf  
  
ENV ELASTICSEARCH_IP 127.0.0.1  
  
ENV LOGSTASH_VERSION 1.5.0.rc2  
  
RUN yum update -y && \  
yum install -y tar java-1.7.0-openjdk openssl && \  
yum clean all && \  
mkdir -p /opt/logstash/ssl && \  
cd /opt/logstash && \  
curl -O
https://download.elasticsearch.org/logstash/logstash/logstash-$LOGSTASH_VERSION.tar.gz
&& \  
tar zxvf logstash-$LOGSTASH_VERSION.tar.gz -C /opt/logstash --strip-
components=1 && \  
rm logstash-$LOGSTASH_VERSION.tar.gz && \  
cd /opt/logstash/ssl && \  
openssl req -x509 -batch -nodes -days 3650 -newkey rsa:2048 -keyout logstash-
forwarder.key -out logstash-forwarder.crt  
  
ADD supervisord.conf /etc/supervisor.d/logstash.conf  
  
VOLUME ["/etc/logstash.d", "/opt/logstash/ssl"]  
  
EXPOSE 5000  


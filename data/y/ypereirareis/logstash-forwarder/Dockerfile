FROM phusion/baseimage  
MAINTAINER Yannick Pereira-Reis http://ypereirareis.github.io  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SSL_DIRECTORY /etc/ssl  
ENV LOGS_DIRECTORY /var/log/forwarder  
  
RUN apt-get update && \  
apt-get install -y build-essential curl git  
  
# Elasticsearch  
RUN \  
apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4 && \  
echo 'deb http://packages.elasticsearch.org/logstashforwarder/debian stable
main' | tee /etc/apt/sources.list.d/logstashforwarder.list && \  
apt-get update  
  
# Logstash forwarder  
RUN apt-get install --no-install-recommends -y logstash-forwarder && \  
apt-get clean  
  
RUN mkdir -p $SSL_DIRECTORY  
ADD ./ssl/logstash-forwarder.crt $SSL_DIRECTORY/logstash-forwarder.crt  
  
RUN mkdir -p $LOGS_DIRECTORY  
  
ADD ./conf/config.json /etc/logstash-forwarder/config.json  
  
CMD [ "/opt/logstash-forwarder/bin/logstash-forwarder", "-config",
"/etc/logstash-forwarder/config.json" ]  


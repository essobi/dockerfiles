FROM dockerfile/java:oracle-java8  
MAINTAINER Patrick Poulain <docker@m41l.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# INSTALL  
RUN apt-get update  
RUN apt-get install -y curl wget  
## Redis  
RUN apt-get install -y redis-server  
  
## Elasticsearch  
RUN \  
wget -qO - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key
add - && \  
if ! grep "elasticsearch" /etc/apt/sources.list; then echo "deb
http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main" >>
/etc/apt/sources.list;fi && \  
if ! grep "logstash" /etc/apt/sources.list; then echo "deb
http://packages.elasticsearch.org/logstash/1.4/debian stable main" >>
/etc/apt/sources.list;fi && \  
apt-get update  
RUN apt-get install -y elasticsearch  
  
## Logstash  
RUN apt-get install -y logstash  
  
## Supervisor  
RUN apt-get install -y supervisor  
  
# CLEANING  
RUN apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# CONFIGURATION  
## Redis  
ADD etc/supervisor/conf.d/redis-server.conf /etc/supervisor/conf.d/redis-
server.conf  
  
## Elasticsearch  
RUN \  
sed -i '/#cluster.name:.*/a cluster.name: logstash'
/etc/elasticsearch/elasticsearch.yml && \  
sed -i '/#path.data: \/path\/to\/data/a path.data: /data'
/etc/elasticsearch/elasticsearch.yml && \  
/usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head  
ADD etc/supervisor/conf.d/elasticsearch.conf
/etc/supervisor/conf.d/elasticsearch.conf  
  
## Logstash  
ADD etc/logstash/logstash.conf /etc/logstash/logstash.conf  
ADD etc/supervisor/conf.d/logstash.conf /etc/supervisor/conf.d/logstash.conf  
  
EXPOSE 6379 9200  
CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]


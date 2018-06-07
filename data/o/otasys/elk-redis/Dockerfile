FROM otasys/java:1.8.0_66  
MAINTAINER Ahmed Hassanien <eng.ahmedgaber@gmail.com>  
  
WORKDIR /opt  
  
# Prerequisites  
## Upgrade ubuntu to latest  
ENV DEBIAN_FRONTEND noninteractive  
  
## Add ELK key to ubuntu repository  
RUN wget -qO - https://packages.elasticsearch.org/GPG-KEY-elasticsearch | sudo
apt-key add -  
## Add Elastic Search Repository to Ubuntu  
RUN add-apt-repository "deb
http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main"  
## Add Log Stash Repository to Ubuntu  
RUN add-apt-repository "deb
http://packages.elasticsearch.org/logstash/1.4/debian stable main"  
## Add Oracle Java 8 Repository to Ubuntu  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
RUN add-apt-repository -y ppa:webupd8team/java  
  
## Update after changing the sources list  
RUN apt-get -q update  
  
# Installing the ELK stack  
# Install Redis  
RUN apt-get -yq install redis-server  
# Redis configuration  
RUN sed -i 's/bind 127.0.0.1/bind 0.0.0.0/g' /etc/redis/redis.conf  
  
# Install Elastic Search  
RUN apt-get -yq install elasticsearch  
## Configuring Elastic Search  
### Add cluster name and Add node name  
RUN sed -i 's/#cluster.name: elasticsearch/cluster.name: elasticsearch/g'
/etc/elasticsearch/elasticsearch.yml  
RUN sed -i 's/#node.name: "Franz Kafka"/node.name: "logstash"/g'
/etc/elasticsearch/elasticsearch.yml  
### Allow Kibana to connect to Elastic Search  
RUN echo 'http.cors.allow-origin: "/.*/"' | tee -a
/etc/elasticsearch/elasticsearch.yml  
RUN echo 'http.cors.enabled: true' | tee -a
/etc/elasticsearch/elasticsearch.yml  
### Move elastic search configurations to the right place  
RUN mkdir /usr/share/elasticsearch/config  
RUN cp /etc/elasticsearch/*.yml /usr/share/elasticsearch/config  
  
# Install Log Stash  
RUN apt-get -yq install logstash  
## Configuring Log Stash  
### Indexer configuration  
ADD ./logstash/logstash-indexer.conf /etc/logstash/conf.d/logstash-
indexer.conf  
  
# Install Supervisor  
RUN apt-get -yq install supervisor  
ADD ./supervisor/elasticsearch.conf /etc/supervisor/conf.d/  
ADD ./supervisor/logstash.conf /etc/supervisor/conf.d/  
ADD ./supervisor/kibana.conf /etc/supervisor/conf.d/  
ADD ./supervisor/redis.conf /etc/supervisor/conf.d/  
  
# Remove unwanted applications & Clean Installations  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Exposing Redis Server Port, Kibana Port and SYSLOG Port  
EXPOSE 6379  
EXPOSE 9292  
EXPOSE 9200  
# Start supervisor  
CMD /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf  


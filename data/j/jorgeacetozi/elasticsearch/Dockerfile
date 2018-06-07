# Set the base image to java8  
FROM openjdk:8-jre  
  
# File Author / Maintainer  
MAINTAINER Jorge Acetozi  
  
# Define default environment variables  
ENV ELASTICSEARCH_VERSION=5.6.6  
ENV ELASTICSEARCH_HOME=/opt/elasticsearch  
  
# Create elasticsearch group and user  
RUN groupadd -g 1000 elasticsearch \  
&& useradd -d "$ELASTICSEARCH_HOME" -u 1000 -g 1000 -s /sbin/nologin
elasticsearch  
  
# Install Elasticsearch 5.6.6  
RUN wget
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz
-P /opt \  
&& cd /opt \  
&& tar xvzf elasticsearch-$ELASTICSEARCH_VERSION.tar.gz \  
&& mv elasticsearch-$ELASTICSEARCH_VERSION elasticsearch \  
&& rm -f elasticsearch-$ELASTICSEARCH_VERSION.tar.gz \  
&& mkdir -p /var/data/elasticsearch \  
&& mkdir -p /var/log/elasticsearch  
  
WORKDIR $ELASTICSEARCH_HOME  
  
# Add initialization script  
ADD bin/docker-entrypoint.sh bin/docker-entrypoint.sh  
  
# Add configuration files  
ADD config/* config/  
  
# Change directories ownership to elasticsearch user and group  
RUN chown -R elasticsearch:elasticsearch $ELASTICSEARCH_HOME
/var/data/elasticsearch /var/log/elasticsearch  
  
# Run the container as elasticsearch user  
USER elasticsearch  
  
# Define mountable directories  
VOLUME /var/data/elasticsearch  
VOLUME /var/log/elasticsearch  
  
# Exposes ports  
EXPOSE 9200 9300  
# Define main command  
ENTRYPOINT ["/opt/elasticsearch/bin/docker-entrypoint.sh"]  


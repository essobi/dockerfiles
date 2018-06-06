#######################################################  
# Dockerfile to build Elasticsearch 5.5.1 environment #  
#######################################################  
  
# Set the base image to openjdk:8-jre  
FROM openjdk:8-jre  
  
# File Author / Maintainer  
MAINTAINER Roberto Besser <rmbesser@gmail.com>  
  
# Run as a root user  
USER root  
  
# Setting some environment variables up  
ENV ELASTICSEARCH_VERSION 5.6.1  
ENV ELASTICSEARCH_HOME=/opt/elasticsearch  
  
# Installing sudo module to support Logstash installation  
RUN apt-get update && \  
apt-get -y install sudo vim curl  
  
# Installing Elasticsearch  
RUN wget
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz
-P /tmp/elasticsearch && \  
tar -xvzf /tmp/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz -C
/tmp/elasticsearch && \  
rm -rf /tmp/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz && \  
mv /tmp/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION $ELASTICSEARCH_HOME
&& \  
rm -rf /tmp/elasticsearch  
  
# Changing the path to HOME  
WORKDIR "$ELASTICSEARCH_HOME"  
  
# Install Elasticsearch monitoring plugins  
RUN ./bin/elasticsearch-plugin install x-pack  
  
# Creates directory used to store the data files  
RUN mkdir -p /var/data/elasticsearch  
  
# Creates directory used to store the log files  
RUN mkdir -p /var/log/elasticsearch  
  
# Create elasticsearch group and user  
RUN groupadd -g 1000 elasticsearch \  
&& useradd -d "$ELASTICSEARCH_HOME" -u 1000 -g 1000 -s /sbin/nologin
elasticsearch  
  
# Adding a entrypoint file to inside the image  
ADD bin/entrypoint.sh /opt/elasticsearch/bin/docker-entrypoint.sh  
  
# Adding a configuration file to inside the image  
ADD config/elasticsearch.yml /opt/elasticsearch/config/elasticsearch.yml  
  
# Changing the permission of the .sh entrypoint file to allow execution  
RUN chmod 755 /opt/elasticsearch/bin/docker-entrypoint.sh  
  
# Changing the owner for config data and log folders  
RUN chown -R elasticsearch:elasticsearch /opt/elasticsearch/config/
/var/data/elasticsearch /var/log/elasticsearch  
  
# Run the container as elasticsearch user  
USER elasticsearch  
  
# Entrypoint file for this image  
ENTRYPOINT ["/opt/elasticsearch/bin/docker-entrypoint.sh"]  
  
# Exposes http ports  
EXPOSE 9200 9300  


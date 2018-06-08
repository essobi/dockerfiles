# PixelHyperlink Elasticsearch Docker  
#  
# VERSION 1.2.0  
FROM pixelhyperlinkdockers/javajdk:v1.1.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with Java JDK and
Elasticsearch service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.2.0"  
LABEL com.pixelhyperlink.docker.elasticsearch.version="1.2.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.elasticsearch.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.elasticsearch.version.is-production="true"  
  
ENV CLUSTER_NAME pixelhyperlink-prod  
ENV ES_SKIP_SET_KERNEL_PARAMETERS true  
  
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \  
apt-key add - && \  
apt-get -y install apt-transport-https && \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | \  
tee -a /etc/apt/sources.list.d/elastic-5.x.list && \  
apt-get update && \  
apt-get -y install elasticsearch  
  
EXPOSE 9200-9300  
VOLUME ["/var/lib/elasticsearch", "/var/log/elasticsearch"]  
  
# Copy logstash config.  
COPY ./elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
  
RUN chmod 755 /etc/elasticsearch/elasticsearch.yml  
  
COPY ./elasticsearch_entrypoint.sh /opt/elasticsearch_entrypoint.sh  
  
# Run startup scripts  
RUN chmod 777 /opt/elasticsearch_entrypoint.sh  
  
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-geoip  
  
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-user-
agent  
  
USER elasticsearch  
  
ENTRYPOINT ["/opt/elasticsearch_entrypoint.sh"]  


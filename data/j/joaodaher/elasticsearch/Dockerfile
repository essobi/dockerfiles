# Dockerfile for Elasticsearch (Kubernetes-Ready)  
# Elasticsearch 5.4.1  
  
# Build with:  
# docker build -t joaodaher/elasticsearch .  
  
# Run with:  
# docker run -p 9200:9200 -it --name elk joaodaher/elasticsearch  
  
FROM quay.io/pires/docker-elasticsearch:5.4.1  
MAINTAINER Joao Daher <joao.daher.neto@gmail.com>  
ENV REFRESHED_AT 2017-06-10  
  
  
  
###############################################################################  
# CONFIGURATION  
###############################################################################  
  
### configure Elasticsearch  
  
ENV DISCOVERY_SERVICE elasticsearch-discovery  
  
ADD config /elasticsearch/config  
ADD ./plugins/hunspell /elasticsearch/config/hunspell  
ADD ./plugins/geoip /elasticsearch/config/ingest-geoip  
#ADD ./plugins/analysis-phonetic-${ES_VERSION}.zip /tmp  
  
ENV ES_PLUGINS_INSTALL ingest-attachment,ingest-geoip,ingest-user-
agent,repository-gcs


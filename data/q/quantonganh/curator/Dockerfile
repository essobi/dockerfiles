# Docker Definition for ElasticSearch Curator  
FROM python:2.7.8-slim  
MAINTAINER Christian R. Vozar <christian@rogueethic.com>  
  
RUN apt-get update && \  
apt-get -y install gettext-base && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install --quiet elasticsearch-curator  
  
ENV ELASTICSEARCH_CLEANUP_HOST="elasticsearch" \  
ELASTICSEARCH_CLEANUP_PORT=9200 \  
ELASTICSEARCH_CLEANUP_USE_SSL=False \  
ELASTICSEARCH_CLEANUP_SSL_NO_VALIDATE=False \  
ELASTICSEARCH_CLEANUP_HTTP_AUTH="elastic:changeme" \  
ELASTICSEARCH_CLEANUP_INDICES_PREFIX="logstash-" \  
ELASTICSEARCH_CLEANUP_OLDER_THAN_UNIT="days" \  
ELASTICSEARCH_CLEANUP_OLDER_THAN_UNIT_COUNT=45 \  
ELASTICSEARCH_CLEANUP_WAIT_TIMEOUT=15  
ADD curator.tpl curator.tpl  
ADD delete_indices.tpl delete_indices.tpl  
  
COPY wait-for-it.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/wait-for-it.sh  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  


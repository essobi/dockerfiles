FROM java:8-jre  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get clean  
  
RUN cd / && \  
curl -O
https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.2.0/elasticsearch-2.2.0.tar.gz
&& \  
tar xf elasticsearch-2.2.0.tar.gz && \  
rm elasticsearch-2.2.0.tar.gz && \  
cd elasticsearch-2.2.0 && bin/plugin install license && bin/plugin install
watcher && \  
useradd -u 1000 elasticsearch  
  
COPY elasticsearch.yml /elasticsearch-2.2.0/config/elasticsearch.yml  
COPY run.sh /  
COPY elasticsearch_logging_discovery /  
  
RUN chmod +x /run.sh /elasticsearch_logging_discovery && mkdir /data && chown
elasticsearch /data  
  
VOLUME ["/data"]  
EXPOSE 9200 9300  
CMD ["/run.sh"]  


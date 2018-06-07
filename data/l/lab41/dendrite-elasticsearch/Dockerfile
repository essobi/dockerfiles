FROM lab41/dendrite-cdh5  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
# elasticsearch  
RUN wget --no-check-certificate
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.5.deb  
RUN dpkg -i elasticsearch-0.90.5.deb; \  
rm -rf elasticsearch-0.90.5.deb  
RUN echo 'discovery.zen.ping.multicast.enabled: false' >>
/etc/elasticsearch/elasticsearch.yml; \  
echo 'node.local: false' >> /etc/elasticsearch/elasticsearch.yml; \  
echo 'index.number_of_shards: 1' >> /etc/elasticsearch/elasticsearch.yml; \  
echo 'index.number_of_replicas: 0' >> /etc/elasticsearch/elasticsearch.yml; \  
echo 'script.disable_dynamic: true' >> /etc/elasticsearch/elasticsearch.yml  
ADD elasticsearch.conf /etc/supervisor/conf.d/elasticsearch.conf  


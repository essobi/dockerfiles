FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.3  
  
RUN touch /usr/share/elasticsearch/config/elasticsearch.yml && \  
echo -n > /usr/share/elasticsearch/config/elasticsearch.yml && \  
echo "cluster.name: 'docker-cluster'" >>
/usr/share/elasticsearch/config/elasticsearch.yml && \  
echo "network.host: 0.0.0.0" >>
/usr/share/elasticsearch/config/elasticsearch.yml && \  
echo "discovery.type: 'single-node'" >>
/usr/share/elasticsearch/config/elasticsearch.yml && \  
echo "discovery.zen.minimum_master_nodes: 1" >>
/usr/share/elasticsearch/config/elasticsearch.yml  


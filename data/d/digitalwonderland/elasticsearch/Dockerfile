# Elasticsearch  
FROM digitalwonderland/base:latest  
  
ADD src/ /  
RUN chmod +x /usr/local/sbin/start.sh  
  
# Install Elasticsearch  
RUN yum install -y elasticsearch jna which && yum clean all;  
  
# Install Kibana  
RUN /usr/share/elasticsearch/bin/plugin -url
https://download.elasticsearch.org/kibana/kibana/kibana-3.1.2.zip -install
elasticsearch/kibana3  
  
# Install Marvel - only free for Development!  
RUN /usr/share/elasticsearch/bin/plugin -i elasticsearch/marvel/latest;  
  
EXPOSE 9200 9300  
VOLUME ["/etc/elasticsearch", "/var/lib/elasticsearch",
"/var/log/elasticsearch"]  
  
ENTRYPOINT ["/usr/local/sbin/start.sh"]  


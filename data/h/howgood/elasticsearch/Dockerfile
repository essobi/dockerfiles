# howgood/elasticsearch  
# Pull base image.  
FROM elasticsearch:1.7  
# Install the AWS plugin  
RUN /usr/share/elasticsearch/bin/plugin install \  
elasticsearch/elasticsearch-cloud-aws/2.7.0  
  
COPY elasticsearch.yml /usr/share/elasticsearch/config/  


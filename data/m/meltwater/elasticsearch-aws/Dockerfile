# Pull base image.  
FROM elasticsearch:1.5  
# Install HEAD plugin  
RUN /usr/share/elasticsearch/bin/plugin install elasticsearch/elasticsearch-
cloud-aws/2.5.0  
  
# Add default config file  
ADD elasticsearch.yml /usr/share/elasticsearch/config/  


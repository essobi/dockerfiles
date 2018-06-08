#  
# ElasticSearch Dockerfile  
#  
# https://github.com/dockerfile/elasticsearch  
#  
# Pull base image.  
FROM dockerfile/java:oracle-java7  
  
# Install ElasticSearch.  
RUN \  
cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.0.1.tar.gz
&& \  
tar xvzf elasticsearch-1.0.1.tar.gz && \  
rm -f elasticsearch-1.0.1.tar.gz && \  
mv /tmp/elasticsearch-1.0.1 /elasticsearch && \  
cd /elasticsearch && \  
bin/plugin -install elasticsearch/elasticsearch-mapper-attachments/2.0.0 && \  
bin/plugin -install com.github.kzwang/elasticsearch-image/1.2.0  
# Define default command.  
CMD ["/elasticsearch/bin/elasticsearch"]  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300  


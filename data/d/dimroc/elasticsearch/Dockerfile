#  
# ElasticSearch Dockerfile  
#  
# https://github.com/dockerfile/elasticsearch  
#  
# Pull base image.  
FROM dockerfile/java:oracle-java6  
  
# Install ElasticSearch.  
RUN \  
cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.13.tar.gz
&& \  
mv elasticsearch-0.90.13.tar.gz elasticsearch.tar.gz && \  
mkdir /tmp/elasticsearch && \  
tar xvzf elasticsearch.tar.gz -C /tmp/elasticsearch --strip-components=1 && \  
rm -f elasticsearch.tar.gz && \  
mv /tmp/elasticsearch /elasticsearch  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Mount elasticsearch.yml config  
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
ENTRYPOINT ["/elasticsearch/bin/elasticsearch"]  
CMD ["-f"]  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300  


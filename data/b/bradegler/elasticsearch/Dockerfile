FROM bradegler/java7  
  
# Install ElasticSearch.  
RUN \  
cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.2.tar.gz
&& \  
tar xvzf elasticsearch-1.3.2.tar.gz && \  
rm -f elasticsearch-1.3.2.tar.gz && \  
mv /tmp/elasticsearch-1.3.2 /elasticsearch  
  
# Define mountable directories.  
VOLUME ["/data/data"]  
  
# Mount elasticsearch.yml config  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
RUN /elasticsearch/bin/plugin -i elasticsearch/marvel/latest  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["/elasticsearch/bin/elasticsearch"]  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300


FROM elasticsearch:1.3  
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
  
# Install plugins  
RUN \  
plugin -i mobz/elasticsearch-head && \  
plugin -i elasticsearch/elasticsearch-river-couchdb/2.3.0 && \  
plugin -i elasticsearch/elasticsearch-lang-javascript/2.3.1 && \  
plugin -i elasticsearch/elasticsearch-analysis-icu/2.3.0  


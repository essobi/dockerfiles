FROM solr:6.0.1  
EXPOSE 8983  
ENV SOLR_HOME="/data/solr"  
VOLUME ["/data/solr"]  
  
COPY entrypoint/* /docker-entrypoint-initdb.d/  


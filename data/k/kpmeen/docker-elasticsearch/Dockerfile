FROM docker.elastic.co/elasticsearch/elasticsearch:6.2.4  
ENV xpack.security.enabled=false  
ENV ES_JAVA_OPTS="-Xms512m -Xmx512m"  
RUN bin/elasticsearch-plugin install ingest-attachment  
  
EXPOSE 9200 9300  


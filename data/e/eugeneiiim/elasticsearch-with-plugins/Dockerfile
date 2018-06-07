# DOCKER-VERSION 1.0  
FROM barnybug/elasticsearch:1.4.2  
RUN /elasticsearch/bin/plugin -install mobz/elasticsearch-head  
RUN /elasticsearch/bin/plugin -install lukas-vlcek/bigdesk  
RUN /elasticsearch/bin/plugin -install royrusso/elasticsearch-HQ  
  
ENV ES_HEAP_SIZE 1G  
  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  


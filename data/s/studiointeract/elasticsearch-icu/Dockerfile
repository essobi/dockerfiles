FROM docker.elastic.co/elasticsearch/elasticsearch:5.4.0  
ADD elasticsearch.yml /usr/share/elasticsearch/config/  
  
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu  
RUN bin/elasticsearch-plugin remove x-pack  
  


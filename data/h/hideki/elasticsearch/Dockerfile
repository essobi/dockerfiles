FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.4  
  
RUN elasticsearch-plugin install analysis-kuromoji && \  
elasticsearch-plugin install analysis-icu  
  
COPY config/elasticsearch.yml /usr/share/elasticsearch/config/  
USER root  
RUN chown elasticsearch:elasticsearch
/usr/share/elasticsearch/config/elasticsearch.yml  
USER elasticsearch  


FROM elasticsearch:1.4.4  
MAINTAINER kristen.gilden@i-smith.ee  
  
COPY elasticsearch.yml ./config/elasticsearch.yml  
ENV ES_HEAP_SIZE=64m  
ENV MAX_LOCKED_MEMORY=50000  
RUN /usr/share/elasticsearch/bin/plugin install elasticsearch/elasticsearch-
mapper-attachments/2.4.3  
RUN /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head  
  


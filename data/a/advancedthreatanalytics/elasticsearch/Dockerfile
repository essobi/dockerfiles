FROM elasticsearch:2.1.2  
  
RUN /usr/share/elasticsearch/bin/plugin install cloud-aws  
RUN /usr/share/elasticsearch/bin/plugin install lmenezes/elasticsearch-
kopf/2.0  
  
COPY config /usr/share/elasticsearch/config  


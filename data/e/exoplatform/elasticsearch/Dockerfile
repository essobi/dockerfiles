FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.3  
  
ENV xpack.security.enabled=false  
  
RUN cd /usr/share/elasticsearch \  
&& bin/elasticsearch-plugin install -b -s ingest-attachment \  
&& bin/elasticsearch-plugin install -b -s mapper-attachments  
  
COPY jvm.options /usr/share/elasticsearch/config/  


FROM docker.elastic.co/elasticsearch/elasticsearch:5.4.2  
  
RUN set -ex \  
&& elasticsearch-plugin remove x-pack \  
&& rm -rf /usr/share/elasticsearch/config/x-pack  


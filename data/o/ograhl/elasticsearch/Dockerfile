FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.8  
# (Un-)Install plugins  
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin remove x-pack --purge &&
\  
yes | /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-
attachment  


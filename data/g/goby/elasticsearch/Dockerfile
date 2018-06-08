FROM elasticsearch:2.4.4-alpine  
  
# Listen on first non-loopback device  
ADD elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
  
# Make sure ES can read this configuration  
RUN chmod a+r /usr/share/elasticsearch/config/elasticsearch.yml  


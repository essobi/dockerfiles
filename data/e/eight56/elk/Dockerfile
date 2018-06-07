FROM willdurand/elk  
  
ADD logstash.conf /etc/logstash/logstash.conf  
  
# /data_logstash contient les certificats pour logstash-forwarder  
VOLUME ["/var/data/elasticsearch", "/data_logstash"]  


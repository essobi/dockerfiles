FROM docker.elastic.co/logstash/logstash:6.2.4  
RUN /opt/logstash/bin/logstash-plugin install logstash-filter-truncate  
RUN /opt/logstash/bin/logstash-plugin install logstash-filter-range  
RUN /opt/logstash/bin/logstash-plugin install logstash-filter-json_encode  


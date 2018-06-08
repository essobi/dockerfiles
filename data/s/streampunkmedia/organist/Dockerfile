FROM docker.elastic.co/logstash/logstash:5.4.0  
# Remove x-pack as it is not supported by Amazon ES  
RUN /usr/share/logstash/bin/logstash-plugin remove x-pack  
  
# Add output plugin for Amazon ES  
RUN /usr/share/logstash/bin/logstash-plugin install logstash-output-amazon_es  
  
# Remove default configuration files  
RUN rm -f /usr/share/logstash/pipeline/logstash.conf  
RUN rm -f /usr/share/logstash/config/logstash.yml  
  
# Add required configuration files  
ADD pipeline/ /usr/share/logstash/pipeline/  
ADD config/ /usr/share/logstash/config/  


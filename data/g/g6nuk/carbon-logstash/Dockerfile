FROM docker.elastic.co/logstash/logstash:5.5.2  
RUN logstash-plugin install logstash-input-beats  
RUN rm -f /usr/share/logstash/pipeline/logstash.conf  
ADD pipeline/ /usr/share/logstash/pipeline/  
ADD config/ /usr/share/logstash/config/  
RUN logstash-plugin install logstash-input-beats  


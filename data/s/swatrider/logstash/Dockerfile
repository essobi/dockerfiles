FROM docker.elastic.co/logstash/logstash:5.2.2  
RUN rm -f /usr/share/logstash/pipeline/logstash.conf  
COPY elasticsearch_template.json /etc/logstash/template/  
ADD pipeline/ /usr/share/logstash/pipeline/  
ADD config/ /usr/share/logstash/config/  


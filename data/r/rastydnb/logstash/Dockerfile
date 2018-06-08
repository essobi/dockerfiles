FROM docker.elastic.co/logstash/logstash:5.3.0  
  
RUN rm -f /usr/share/logstash/pipeline/logstash.conf  
ADD pipeline/ /usr/share/logstash/pipeline/  
ADD config/ /usr/share/logstash/config/  
  
USER root  
RUN apt-get update && apt-get install -y vim  
RUN chown logstash:logstash /usr/share/logstash/pipeline/logstash.conf &&
chown logstash:logstash /usr/share/logstash/config/logstash.yml  
  
  


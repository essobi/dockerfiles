FROM logstash:2  
RUN logstash-plugin install logstash-input-rabbitmq logstash-output-mongodb  
  
COPY lsrmq2mongo.conf /etc/logstash/  
  
CMD ["-f", "/etc/logstash/lsrmq2mongo.conf","--debug"]  


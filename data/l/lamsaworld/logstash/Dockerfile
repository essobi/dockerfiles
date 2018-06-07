FROM logstash  
  
COPY config/logstash.conf /etc/logstash/conf.d/logstash.conf  
  
RUN logstash-plugin install logstash-filter-de_dot  
  
EXPOSE 5000  
CMD ["-f", "/etc/logstash/conf.d/logstash.conf"]  


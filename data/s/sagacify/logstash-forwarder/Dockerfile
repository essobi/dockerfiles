FROM logstash:2.4.0-1  
RUN logstash-plugin install --no-verify \  
logstash-filter-de_dot \  
logstash-filter-environment \  
logstash-input-cloudwatch  
  
ADD logstash-logs.conf /var/logstash/logstash-logs.conf  
ADD logstash-cloudwatch.conf /var/logstash/logstash-cloudwatch.conf  
  
CMD ["logstash", "-f", "/var/logstash/logstash-logs.conf"]  


FROM logstash:2.4.1  
ADD ./logstash-config /logstash-config  
  
ENTRYPOINT ["logstash", "agent", "-f", "/logstash-config/", "--debug"]  


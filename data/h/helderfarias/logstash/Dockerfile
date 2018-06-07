FROM logstash:2.4.0  
ADD logstash.conf /etc/logstash  
  
VOLUME /etc/logstash  
  
EXPOSE 5000  
EXPOSE 5044  
EXPOSE 12201  
CMD ["-f", "/etc/logstash/logstash.conf"]  


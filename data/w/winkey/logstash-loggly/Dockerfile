FROM logstash:2.4  
RUN logstash-plugin install logstash-output-loggly  
ADD logstash.conf /etc/  
  
CMD [ "-f", "/etc/logstash.conf" ]  


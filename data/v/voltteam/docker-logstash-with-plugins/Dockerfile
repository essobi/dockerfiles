FROM docker.elastic.co/logstash/logstash:5.5.0  
RUN echo xpack.monitoring.enabled: false >>
./usr/share/logstash/config/logstash.yml  
# ENV JAVA_OPTS=-Djava.security=file:/dev/urandom  
RUN logstash-plugin install logstash-output-amazon_es  
  
CMD ["-f", "/config/logstash.conf"]  


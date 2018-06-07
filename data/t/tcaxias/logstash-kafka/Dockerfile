# Container for Logstash with upgraded Kafka Input  
FROM logstash:5  
MAINTAINER Tiago Caxias http://github.com/tcaxias  
RUN logstash-plugin update logstash-input-kafka  
RUN logstash-plugin update logstash-output-kafka  
RUN logstash-plugin update logstash-input-syslog  


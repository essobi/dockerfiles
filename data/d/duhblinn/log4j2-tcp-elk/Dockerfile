FROM willdurand/elk  
MAINTAINER Wynand Pieters <wynandpieters@gmail.com>  
  
VOLUME ["/etc/logstash"]  
  
COPY conf /etc/logstash  
  
RUN /opt/logstash/bin/plugin install logstash-input-tcp &
/opt/logstash/bin/plugin install logstash-input-log4j2  
  
EXPOSE 7000  
EXPOSE 5959


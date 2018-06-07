FROM leprechaun/logstash-base  
  
RUN /opt/logstash/bin/plugin install logstash-input-kinesis-cloudwatch-log-
subscription  
RUN /opt/logstash/bin/plugin install logstash-codec-cloudwatch-log-
subscription  
  
RUN /opt/logstash/bin/plugin install logstash-output-kinesis-leprechaun-fork  


FROM logstash:2  
RUN logstash-plugin install logstash-output-mongodb  
  
COPY logstash-enqueue.conf /etc/logstash/  
COPY logstash-persist.conf /etc/logstash/  
  
CMD logstash -f /etc/logstash/logstash-${LOGSTASH_MODE}.conf --debug  


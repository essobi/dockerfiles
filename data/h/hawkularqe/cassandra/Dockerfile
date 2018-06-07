FROM cassandra:3.9  
env LOG_DIR /var/log/cassandra  
  
RUN mkdir -p "$LOG_DIR" \  
&& chown -R cassandra:cassandra "$LOG_DIR" \  
&& chmod 777 "$LOG_DIR"  
  
COPY docker-start.sh /docker-start.sh  
  
ENTRYPOINT ["/docker-start.sh"]  


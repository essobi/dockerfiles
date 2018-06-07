FROM logstash:5.4.0  
ADD ./logstash.conf /etc/logstash/logstash.conf  
  
EXPOSE 2056  
EXPOSE 2057/udp  
EXPOSE 8514  
EXPOSE 8514/udp  
  
ENTRYPOINT ["/docker-entrypoint.sh", "-f", "/etc/logstash/logstash.conf"]  


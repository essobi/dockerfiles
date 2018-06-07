FROM logstash:latest  
EXPOSE 5000 5001 55514/udp  
COPY ./logstash.conf /etc/logstash.d/logstash.conf  
  
ADD run.sh /opt/run.sh  
  
CMD ["/opt/run.sh"]  


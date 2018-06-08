FROM logstash:2.3  
COPY logstash.conf gracc-raw-template.json /etc/gracc-stash/  
  
CMD ["-f", "/etc/gracc-stash/logstash.conf","--allow-env"]  


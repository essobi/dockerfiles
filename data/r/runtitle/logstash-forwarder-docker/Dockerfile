FROM digitalwonderland/logstash-forwarder  
  
VOLUME ["/opt/conf", "/opt/certs"]  
  
CMD ["/usr/local/bin/docker-logstash-forwarder", "-quiet", "-config",
"/opt/conf/config.json"]  


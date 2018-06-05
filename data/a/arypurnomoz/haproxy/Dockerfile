FROM haproxy  
  
ENV LOG_HOST localhost  
ENV CONFD_OPTS "-interval=10"  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 /usr/local/bin/confd  
  
RUN chmod +x /usr/local/bin/confd  
  
ADD run.sh /tmp/run.sh  
  
ENTRYPOINT ["/tmp/run.sh"]  


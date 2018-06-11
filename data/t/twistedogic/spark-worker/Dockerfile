FROM twistedogic/spark-base  
MAINTAINER Jordan Li  
  
COPY start.sh /  
COPY supervisord.conf /etc/supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  


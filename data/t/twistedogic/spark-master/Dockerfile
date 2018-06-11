FROM twistedogic/spark-base  
MAINTAINER Jordan Li  
  
COPY start.sh /  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 7077 8080  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  


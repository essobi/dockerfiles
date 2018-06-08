FROM twistedogic/mesos-serf  
MAINTAINER Jordan Li  
  
ADD start.sh /start.sh  
  
ADD supervisord.conf /etc/supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  


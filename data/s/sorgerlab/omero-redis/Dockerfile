FROM redis  
MAINTAINER douglas_russell@hms.harvard.edu  
  
ADD entrypoint.sh /usr/local/bin/  
ADD redis.conf /usr/local/etc/redis/  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  


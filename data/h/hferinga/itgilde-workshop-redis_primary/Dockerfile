FROM hferinga/itgilde-workshop-redis_base  
MAINTAINER James Turnbull <james@example.com>  
ENV REFRESHED_AT 2014-06-01  
VOLUME [ "/var/lib/redis", "/var/log/redis" ]  
  
EXPOSE 6379  
ENTRYPOINT [ "redis-server", "--logfile /var/log/redis/redis-server.log" ]  
  


FROM hferinga/itgilde-workshop-redis_base  
MAINTAINER James Turnbull <james@example.com>  
ENV REFRESHED_AT 2014-06-01  
#VOLUME [ "/var/lib/redis", "/var/log/redis" ]  
ENTRYPOINT [ "redis-server", "--logfile /var/log/redis/redis-replica.log", "--
slaveof redis_primary 6379" ]  


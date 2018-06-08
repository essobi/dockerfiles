FROM shimaore/debian:2.0.7  
MAINTAINER Stéphane Alnet <stephane@shimaore.net>  
  
# Install prereqs  
RUN apt-get update && apt-get --no-install-recommends -y install \  
'redis-server=2:3.0.6-1' \  
&& apt-get autoremove -y && apt-get clean  
COPY start.sh /usr/sbin/start-redis.sh  
  
# Finalize  
USER redis  
EXPOSE 6379  
CMD ["/usr/sbin/start-redis.sh"]  


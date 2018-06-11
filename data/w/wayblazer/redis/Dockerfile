FROM redis:3.0.4  
MAINTAINER Kevin Kuhl kevin@wayblazer.com  
  
RUN apt-get update && apt-get install -y supervisor  
RUN mkdir -p /data/redis /logs/  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
ADD redis.conf /usr/local/etc/redis/redis.conf  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENV SLAVE false  
ENV MASTER_PORT 6379  
VOLUME ["/data", "/logs"]  
EXPOSE 6379 4567  
CMD ["/run.sh"]  


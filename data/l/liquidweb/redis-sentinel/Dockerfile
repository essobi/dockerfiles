FROM ubuntu  
MAINTAINER Dan Burke <dburke@liquidweb.com>  
  
RUN apt-get update && apt-get install -y redis-server redis-sentinel  
RUN apt-get update && apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD sentinel.conf /usr/local/etc/sentinel.conf  
RUN chmod a+rw /usr/local/etc/sentinel.conf /usr/local/etc  
  
EXPOSE 26379  
CMD ["/usr/bin/supervisord"]  
  


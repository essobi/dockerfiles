FROM synopsis/php:cli  
  
RUN apt-get update && apt-get install -y supervisor && apt-get clean  
RUN mkdir -p /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/000-supervisord.conf  
  
VOLUME ["/etc/supervisor/conf.d"]  
  
EXPOSE 9001  
CMD ["/usr/bin/supervisord"]  


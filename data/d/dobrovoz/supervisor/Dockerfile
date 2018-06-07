FROM dobrovoz/php-fpm  
  
VOLUME /var/log/  
  
RUN apt-get update && apt-get install -y supervisor \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD supervisord.conf /etc/supervisord.conf  
  
CMD touch /var/log/supervisor.log && /usr/bin/supervisord -n -c
/etc/supervisord.conf && tail -f /var/log/supervisor.log /var/log/horizon.log


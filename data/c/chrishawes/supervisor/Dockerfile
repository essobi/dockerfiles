FROM chrishawes/php7-redis  
  
RUN apk add --no-cache supervisor && \  
addgroup -S supervisor && adduser -D -S -s /sbin/nologin -G supervisor
supervisor && \  
mkdir -p /etc/supervisor/conf.d && chown -R supervisor:supervisor
/etc/supervisor && \  
/usr/bin/supervisord --version  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
VOLUME ["/etc/supervisor/conf.d"]  
WORKDIR /etc/supervisor/conf.d  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  


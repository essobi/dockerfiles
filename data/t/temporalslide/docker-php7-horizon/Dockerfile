FROM temporalslide/docker-php7-fpm-alpine:latest  
  
RUN apk add --update --no-cache \  
supervisor \  
&& rm -rf /var/cache/apk/*  
  
COPY supervisord.conf /etc/supervisord.conf  
  
RUN export TERM=xterm  
USER root  
  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  


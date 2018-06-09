FROM temporalslide/docker-php7-horizon:latest  
  
COPY supervisord.conf /etc/supervisord.conf  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
RUN export TERM=xterm  
  
USER root  
RUN chmod +x /usr/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  


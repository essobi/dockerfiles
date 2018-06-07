FROM kamaninga/php  
  
COPY conf/supervisord.conf /etc/supervisor.d/supervisord.conf  
  
ENTRYPOINT ["supervisord", "-n", "-c", "/etc/supervisor.d/supervisord.conf"]  


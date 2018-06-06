FROM redis:4-alpine  
  
LABEL maintainer="Claudio Netto <nettoclaudio@ufrj.br>"  
  
COPY files/redis-ha-entrypoint.sh /  
  
RUN chown redis:redis /redis-ha-entrypoint.sh && \  
chmod 540 /redis-ha-entrypoint.sh  
  
USER redis  
  
ENTRYPOINT [ "/redis-ha-entrypoint.sh" ]


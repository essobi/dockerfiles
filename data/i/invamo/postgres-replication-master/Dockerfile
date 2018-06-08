FROM postgres:9.6.1-alpine  
  
ENV PGDATA /data  
  
COPY configs/* /configs/  
  
RUN chmod +x /configs/create_replication_user.sh  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
CMD ["postgres", "-c", "config_file=/configs/1gb-ram.conf",
"-c","hba_file=/configs/pg_hba.conf"]  


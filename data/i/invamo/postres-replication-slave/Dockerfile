FROM postgres:9.6.1-alpine  
  
ENV PGDATA /data  
  
COPY configs/* /configs/  
  
RUN mkdir data_replication  
  
RUN chmod +x /configs/replication_init.sh  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
CMD ["postgres", "-c", "config_file=/configs/1gb-ram.conf",
"-c","hba_file=/configs/pg_hba.conf"]  


  
FROM postgres:9.6  
EXPOSE 5432  
COPY pg_backup_rotated.sh pg_backup.config pg_backup.sh /root/  
RUN chmod u+x /root/*.sh  
  
COPY setup.sh /docker-entrypoint-initdb.d/  
RUN chmod u+x /docker-entrypoint-initdb.d/setup.sh  
  
COPY imago_backup /etc/cron.hourly/  
RUN chmod uog+x /etc/cron.hourly/imago_backup  


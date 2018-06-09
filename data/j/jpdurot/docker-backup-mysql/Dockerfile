FROM debian:jessie  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y --force-yes \  
openssh-client \  
mysql-client \  
sshpass \  
supervisor \  
cron \  
rsyslog \  
postfix \  
&& apt-get clean  
  
# Do not restrict too much MySQL server mode :)  
RUN echo "[mysqld]" >> /etc/mysql/conf.d/sql_mode.cnf  
RUN echo "sql-mode=\"\"" >> /etc/mysql/conf.d/sql_mode.cnf  
  
# Backup scripts  
COPY backup.sh /backup.sh  
COPY backup_job.sh /backup_job.sh  
RUN chmod u+x /backup.sh  
RUN chmod u+x /backup_job.sh  
  
# Backup logs  
# Doesn't work at the moment, Rsyslog does not seem to look at additional conf
files :()  
RUN echo "if \$programname == 'backup' then /var/log/backup.log" >
/etc/rsyslog.d/10-backup.conf  
  
# Run backup every night  
#RUN sed -i '15i* * * * * root . /root/.bashrc ; rm /var/log/backup_job.log ;
/backup_job.sh >> /var/log/backup_job.log 2>&1 \n' /etc/crontab  
RUN sed -i '15i0 0,12 * * * root /bin/bash -c "source /root/.bashrc ;
/backup_job.sh"' /etc/crontab  
  
# Set timezone  
RUN echo "Europe/Paris" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
# Startup script  
COPY run.sh /run.sh  
RUN chmod u+x /run.sh  
  
COPY supervisord.conf /etc/supervisord.conf  
  
CMD ["/run.sh"]  


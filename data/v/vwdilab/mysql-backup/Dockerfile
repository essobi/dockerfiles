FROM ubuntu:16.04  
RUN apt-get update -qqyy  
RUN apt-get install -qqyy jq mysql-client python3-pip cron  
RUN LC_ALL=C LANG=C pip3 install --upgrade pip  
RUN LC_ALL=C LANG=C pip3 install awscli  
  
ADD cron-backup-all-dbs.sh /opt  
ADD dump.sh /opt  
ADD restore.sh /opt  
ADD mysql-console.py /opt  
ADD migrate.py /opt  
  
ADD crontab /etc/cron.d/mysql-backup-cron  
RUN chmod 0644 /etc/cron.d/mysql-backup-cron  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron-mysql-backup.log  
  
CMD echo $VCAP_SERVICES > /root/vcap_services.env && echo $VCAP_APPLICATION >
/root/vcap_app.env && cron && tail -f /var/log/cron-mysql-backup.log  


FROM eaudeweb/cron  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-client ssh rsync
less iputils-ping s-nail ssmtp \  
&& apt-get purge -y --auto-remove  
RUN mkdir /data /root/.ssh /var/log/backup \  
&& chmod 600 /root/.ssh  
  
COPY backup-rsync.sh /usr/local/bin/backup-rsync.sh  
COPY backup-dump-mysql.sh /usr/local/bin/backup-dump-mysql.sh  
COPY test-rsync.sh /usr/local/bin/test-rsync.sh  
COPY test-dump-mysql.sh /usr/local/bin/test-dump-mysql.sh  


FROM postgres:9.6.3  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise main restricted
universe multiverse" >> /etc/apt/sources.list  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise-updates main
restricted universe multiverse" >> /etc/apt/sources.list  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise-backports main
restricted universe multiverse" >> /etc/apt/sources.list  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise-security main
restricted universe multiverse" >> /etc/apt/sources.list  
  
RUN apt-get -y update  
RUN apt-get -y install vim  
  
# Add our entrypoint script for installing extension and creating tables.  
ADD docker-entrypoint-initdb.d/init-user-db.sh /docker-entrypoint-
initdb.d/init-user-db.sh  
  
# Set up our periodic crons for backup up database information  
ADD etc/cron.d/cron.daily/backup-daily-cron /etc/cron.daily/backup-daily-cron  
ADD etc/cron.d/cron.daily/backup-rsync /etc/cron.daily/backup-rsync  
ADD etc/cron.d/cron.monthly/backup-monthly-cron /etc/cron.monthly/backup-
monthly-cron  
  
RUN chmod 0755 /etc/cron.daily/backup-daily-cron  
RUN chmod 0755 /etc/cron.daily/backup-rsync  
RUN chmod 0755 /etc/cron.monthly/backup-monthly-cron  


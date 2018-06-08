FROM postgres:9.6  
MAINTAINER Graeme Gellatly <graemeg@roof.co.nz>  
  
RUN apt-get update && apt-get install -y python3 python3-pip python3-dev lzop
pv daemontools cron  
RUN easy_install3 wal-e  
RUN pip3 install boto  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD initdb.d/setupConfFile.sh /docker-entrypoint-initdb.d/setupConfFile.sh  
ADD initdb.d/setupExtensions.sql /docker-entrypoint-
initdb.d/setupExtensions.sql  
#ADD scripts/setup-wal-e.sh /tmp/setup-wal-e.sh  
RUN chmod 755 /docker-entrypoint-initdb.d/setupConfFile.sh  
RUN chmod 755 /docker-entrypoint-initdb.d/setupExtensions.sql  
#RUN chmod 755 /tmp/setup-wal-e.sh  
#  
#RUN /tmp/setup-wal-e.sh  
#RUN su - postgres -c "crontab -l | { cat; echo \"0 3 * * * /usr/bin/envdir
/etc/wal-e.d/env /usr/local/bin/wal-e backup-push /var/lib/postgresql/data\";
} | crontab -"  
#RUN su - postgres -c "crontab -l | { cat; echo \"30 3 * * * /usr/bin/envdir
/etc/wal-e.d/env /usr/local/bin/wal-e delete --confirm retain 5\"; } | crontab
-"  
#  


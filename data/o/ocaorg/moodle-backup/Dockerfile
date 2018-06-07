FROM platte/dockup:1.0.1  
  
# Expose volumes from Moodle, MariaDB, and the backup volume  
# Add Percona Xtrabackup  
# Add a shell script that fires off Xtrabackup, then copies files from
volumes, then ships the backup files to S3  
# Add cron job that fires that script daily  
  
# Start with Dockup, which provides cron, AWS CLI, and copying  
# Provide pre & post commands that run the DB backup first and delete it
afterward  
  
RUN \  
echo "deb http://repo.percona.com/apt jessie main" >
/etc/apt/sources.list.d/percona.list \  
&& echo "deb-src http://repo.percona.com/apt jessie main" >>
/etc/apt/sources.list.d/percona.list \  
&& apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
1C4CBDCDCD2EFD2A \  
&& apt-get update && apt-get install -y \--no-install-recommends \  
percona-xtrabackup-24 \  
percona-toolkit \  
qpress \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /db-backup  
  
COPY db-backup.sh /db-backup.sh  
  
ENV BEFORE_BACKUP_CMD="/db-backup.sh" \  
AFTER_BACKUP_CMD="rm -r /db-backup/*" \  
CRON_TIME="0 3 * * *"  
  
CMD ["/run.sh"]  


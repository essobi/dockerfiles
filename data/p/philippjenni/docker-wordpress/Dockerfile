FROM philippjenni/docker-amp  
  
MAINTAINER Philipp Jenni <philippjenni@bluemail.ch>  
  
RUN apt-get -y update  
  
#Backup and Restore dirs  
ENV WP_BACKUPDIR=$BACKUPDIR/wordpress  
ENV WP_RESTOREDIR=$RESTOREDIR/wordpress  
  
#Always use mysql for wordpress  
ENV MYSQL_ENABLE true  
  
#File which contains information about either a new performed installation or
about an already existing installation.  
ENV INSTALLATION_FILE_NAME docker-wordpress-installation.state  
ENV INSTALLATION_FILE /$INSTALLATION_FILE_NAME  
  
# Prepare wordpress backup script  
ADD ./wordpressBackup/wordpressBackup.sh /wordpressBackup/wordpressBackup.sh  
RUN chmod 755 /wordpressBackup/wordpressBackup.sh  
ADD ./wordpressBackup/wordpressRestore.sh /wordpressBackup/wordpressRestore.sh  
RUN chmod 755 /wordpressBackup/wordpressRestore.sh  
ADD ./wordpressBackup/crontab /etc/cron.d/wordpressBackup-cron  
RUN chmod 0644 /etc/cron.d/wordpressBackup-cron  
RUN touch /var/log/cron.log  
  
# Add start script  
ADD ./startScripts/start-wordpress.sh /startScripts/start-wordpress.sh  
RUN chmod 755 /startScripts/start-wordpress.sh  
  
CMD ["/startScripts/start-wordpress.sh"]  


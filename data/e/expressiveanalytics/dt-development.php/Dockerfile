FROM expressiveanalytics/dt-standard.php:2.0  
MAINTAINER Jason Cameron <jbkc85@gmail.com>  
  
LABEL version="2.1" \  
description="Debian Image for running Deep Thought.php in Development"  
  
# Adjust permissions of the data folder for SQLite Database  
# and create the basic database  
RUN mkdir -p /var/www/dt-example/storage && \  
sqlite3 /var/www/dt-example/storage/dt-development.db "create table
initdt(deleted integer); drop table initdt;" && \  
chown www-data:staff /var/www/dt-example/storage && chmod 2775 /var/www/dt-
example/storage && \  
chown www-data:staff /var/www/dt-example/storage/dt-development.db && chmod
777 /var/www/dt-example/storage/dt-development.db  
  
# Drop in replacement files for development  
# Enable confs for Logging (PimpMyLogs) and PHPLiteAdmin by Default  
COPY rootfs /  
RUN chmod +x /run.sh && \  
a2enconf pmlviewer phpliteadmin  


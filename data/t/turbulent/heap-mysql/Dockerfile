FROM turbulent/heap-base:2.0.3  
MAINTAINER Benoit Beausejour <b@turbulent.ca>  
  
ENV heap-mysql 2.1.0  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq install mysql-server pwgen && \  
apt-get -yq install percona-xtrabackup && \  
apt-get -yq install unzip && \  
rm -rf /var/lib/apt/lists/*  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# Add MySQL configuration  
ADD mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
ADD import_sql.sh /import_sql.sh  
ADD my.cnf.tmpl /systpl/  
ADD .my.cnf.tmpl /systpl/  
ADD make-backup.sh.tmpl /systpl/  
  
# Innotop  
ADD
https://github.com/innotop/innotop/archive/744710dd39a78a5b25096cd0dcda8ba57a7575b2.zip
/tmp/innotop.zip  
RUN cd /tmp/ && unzip innotop.zip && cd
innotop-744710dd39a78a5b25096cd0dcda8ba57a7575b2 && perl Makefile.PL && make
install  
  
# Add entry scripts  
COPY run.sh /run.sh  
  
RUN chmod 755 /*.sh  
  
# ENV defaults  
ENV VAR_MYSQL_USER=admin \  
VAR_MYSQL_PASS="**Random**" \  
VAR_MYSQL_SLOWLOG="true" \  
VAR_MYSQL_SLOWLOG_TIME="3" \  
VAR_MYSQL_SLOWLOG_INDEXES="0" \  
VAR_MYSQL_SERVER_ID="1" \  
VAR_MYSQL_BINLOG_SIZE="100M" \  
VAR_MYSQL_BINLOG_FORMAT="STATEMENT" \  
VAR_MYSQL_EXPIRE_LOGS_DAYS="14" \  
VAR_MYSQL_MAX_ALLOWED_PACKET="16M" \  
VAR_MYSQL_MAX_CONNECT_ERRORS="100000" \  
VAR_MYSQL_MAX_CONNECTIONS="1024" \  
VAR_MYSQL_OPEN_FILES_LIMIT="65535" \  
VAR_MYSQL_INNODB_BUFFER_POOL_SIZE="100M" \  
VAR_MYSQL_INNODB_ADDITIONAL_MEM_POOL_SIZE="10M" \  
VAR_MYSQL_INNODB_LOG_FILE_SIZE="25M" \  
VAR_MYSQL_INNODB_LOG_BUFFER_SIZE="4M" \  
VAR_MYSQL_INNODB_FLUSH_LOG_AT_TRX_COMMIT="2" \  
VAR_MYSQL_TRANSACTION_ISOLATION="REPEATABLE-READ" \  
VAR_MYSQL_REPLICATION_MASTER="" \  
VAR_MYSQL_REPLICATION_SLAVE="" \  
VAR_MYSQL_REPLICATION_USER="replication" \  
VAR_MYSQL_REPLICATION_PASSWORD="replication" \  
VAR_MYSQL_REPLICATION_HOST="" \  
VAR_MYSQL_REPLICATION_PORT="3306" \  
VAR_MYSQL_BACKUP_DIR=""  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/vol/logs", "/vol/database", "/vol/backups"]  
  
ADD replicactl /replicactl  
  
EXPOSE 3306  
CMD ["/run.sh"]  


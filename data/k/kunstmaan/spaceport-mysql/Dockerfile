FROM percona:5.7  
  
ADD backup.sh /scripts/backup.sh  
RUN chmod -R 755 /scripts  
run rm -rf /etc/mysql/percona-server.conf.d/mysqld.cnf  
ADD mysql-conf.cnf /etc/mysql/percona-server.conf.d/kuma.cnf  


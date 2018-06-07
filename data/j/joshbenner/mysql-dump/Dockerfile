FROM ubuntu:trusty  
MAINTAINER Josh Benner <josh@bennerweb.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
mysql-client && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV MYSQLDUMP_OPTIONS --quote-names --quick --add-drop-table --add-locks
--allow-keywords --disable-keys --extended-insert --single-transaction
--create-options --comments --net_buffer_length=16384  
ENV MYSQL_HOST=**None** \  
MYSQL_PORT=3306 \  
MYSQL_USER=root \  
MYSQL_PASSWORD=**None** \  
MYSQL_BACKUP_DIR=/var/backup/mysql  
  
COPY dump.sh /dump.sh  
  
ENTRYPOINT ["/dump.sh"]  


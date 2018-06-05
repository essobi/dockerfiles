FROM mariadb:10.2  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
#RUN groupadd -r mysql && useradd -r -g mysql mysql  
RUN sed -ri 's/^(bind-address|skip-networking|log)/;\1/' /etc/mysql/my.cnf  
# add configuration  
ADD conf.d/utf8.cnf /etc/mysql/conf.d/utf8.cnf  
ADD conf.d/galera.cnf /etc/mysql/conf.d/galera.cnf  
  
# 3306 - MySQL client connections  
# 4567 - Galera Cluster replication traffic, multicast replication uses both
udp & tcp  
# 4568 - For Incremental State Transfers  
# 4444 - For all other State Snapshot Transfers  
EXPOSE 3306 4444 4567 4568  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# Set TERM env to avoid mysql client error message "TERM environment variable
not set" when running from inside the container  
ENV TERM xterm  
  
# default values for configuration options  
ENV MAX_CONNECTIONS=150 \  
PORT=3306 \  
MAX_ALLOWED_PACKET=16M \  
QUERY_CACHE_SIZE=16M \  
QUERY_CACHE_TYPE=1 \  
INNODB_BUFFER_POOL_SIZE=128M \  
INNODB_LOG_FILE_SIZE=48M \  
INNODB_FLUSH_METHOD= \  
INNODB_OLD_BLOCKS_TIME=1000 \  
INNODB_FLUSH_LOG_AT_TRX_COMMIT=1 \  
INNODB_FILE_FORMAT=Barracuda\  
INNODB_RAW_FORMAT=DYNAMIC\  
SYNC_BINLOG=0  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["mysqld"]  


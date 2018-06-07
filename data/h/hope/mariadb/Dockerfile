FROM hope/base-alpine:3.5  
  
MAINTAINER Sergey Sadovoi <sergey@hope.ua>  
  
ENV \  
MARIADB_VERSION=10.1.20 \  
# Set TERM env to avoid mysql client error message "TERM environment variable
not set" when running from inside the container  
TERM=xterm \  
# Configuration variables  
DB_max_allowed_packet=64M \  
DB_query_cache_size=0 \  
DB_query_cache_type=0 \  
DB_sync_binlog=0 \  
DB_expire_logs_days=3 \  
DB_innodb_buffer_pool_size=768M \  
DB_innodb_log_file_size=128M \  
DB_innodb_flush_method=O_DIRECT \  
DB_innodb_old_blocks_time=1000 \  
DB_innodb_flush_log_at_trx_commit=0 \  
DB_open_files_limit=4096 \  
DB_max_connections=300  
  
COPY rootfs/ /tmp/  
  
RUN \  
# Install and configure MariaDB  
apk add --no-cache mariadb mariadb-client pwgen && \  
echo "" >> /etc/mysql/my.cnf && \  
echo "!includedir /etc/mysql/my.cnf.d" >> /etc/mysql/my.cnf && \  
cp -rf /tmp/etc / && \  
# Entrypoint  
cp -f /tmp/*.sh / && \  
chmod +x /run.sh && \  
# Cleanup  
rm -rf "/tmp/"*  
  
VOLUME /var/lib/mysql  
  
EXPOSE 3306  
  
ENTRYPOINT ["/run.sh"]  


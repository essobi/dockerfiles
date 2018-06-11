FROM benyoo/alpine:3.4.20160812  
MAINTAINER from www.dwhd.org by lookback (mondeolove@gmail.com)  
  
ENV DATA_DIR=/data/mariadb  
  
RUN set -x && \  
[ ! -d "$(dirname ${DATA_DIR})" ] && mkdir -p $(dirname ${DATA_DIR}) && \  
addgroup -S mysql && adduser -S -h ${DATA_DIR} -s /sbin/nologin -G mysql mysql
&& \  
apk --update --no-cache upgrade && \  
apk add --update --no-cache 'su-exec>=0.2' socat rsync xtrabackup lsof
jemalloc-dev nmap mariadb mariadb-client && \  
/bin/rm -rf /etc/my.cnf{,.d} /var/cache/apk/*  
  
#ENV PATH=${INSTALL_DIR}/bin:$PATH \  
ENV TERM=linux \  
MAX_CONNECTIONS=100 \  
PORT1=3306 PORT2=4444 PORT3=4567 PORT4=4568 \  
MAX_ALLOWED_PACKET=16M \  
QUERY_CACHE_SIZE=16M \  
QUERY_CACHE_TYPE=1 \  
INNODB_BUFFER_POOL_SIZE=128M \  
INNODB_LOG_FILE_SIZE=48M \  
INNODB_FLUSH_METHOD= \  
INNODB_OLD_BLOCKS_TIME=1000 \  
INNODB_FLUSH_LOG_AT_TRX_COMMIT=1 \  
SYNC_BINLOG=0  
ADD etc /etc/mysql  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh && \  
sed -i 's/\r$//g' /entrypoint.sh /etc/mysql/my.cnf /etc/mysql/my.cnf.d/* && \  
mkdir -p /var/lib/mysql && \  
chown -R mysql.mysql /var/lib/mysql /etc/mysql  
  
VOLUME ["$DATA_DIR"]  
EXPOSE $PORT1 $PORT2 $PORT3 $PORT4  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["mysqld"]  


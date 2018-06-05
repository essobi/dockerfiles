FROM benyoo/centos:7.2.1511.20160910  
MAINTAINER from www.dwhd.org by lookback (mondeolove@gmail.com)  
  
ARG VERSION=${VERSION:-10.2.2}  
#ARG LOCAL_REPO=${LOCAL_REPO:-disable}  
ENV DATA_DIR=/data/mariadb \  
INSTALL_DIR=/usr/local/mariadb  
  
RUN set -x && \  
[ ! -d "$(dirname ${DATA_DIR})" ] && mkdir -p $(dirname ${DATA_DIR}) && \  
groupadd -r -g 410 mysql && \  
useradd -r -s /sbin/nologin -d /data/mariadb -m -k no -g 410 -u 410 mysql && \  
echo -e "[mariadb]\nname = MariaDB\nbaseurl =
http://yum.mariadb.org/${VERSION}/centos7-amd64\n" >> /tmp/yum.conf && \  
echo -e '[percona]\nname = Percona\nbaseurl =
http://repo.percona.com/release/7/RPMS/x86_64\n' >> /tmp/yum.conf && \  
#sed -i
's@mirrorlist@#&@;s@#baseurl=http://mirror.centos.org@baseurl=http://mirrors.ds.com@'
/etc/yum.repos.d/CentOS-Base.repo && \  
yum -c /tmp/yum.conf install MariaDB-Galera-server MariaDB-client MariaDB-
common galera jemalloc-devel percona-xtrabackup-24 which socat rsync lsof -y
&& \  
yum clean all && \  
rm -rf /var/cache/{yum,ldconfig} /var/lib/mysql/* && \  
mkdir -pv --mode=0755 /var/cache/{yum,ldconfig}  
  
ENV PATH=${INSTALL_DIR}/bin:$PATH \  
TERM=linux \  
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
ADD etc /etc  
COPY entrypoint.sh /entrypoint.sh  
#RUN chmod +x /entrypoint.sh && \  
#sed -i 's/\r$//g' /entrypoint.sh /etc/mysql/my.cnf /etc/mysql/my.cnf.d/* && \  
#mkdir -p /var/lib/mysql && \  
#chown -R mysql.mysql /var/lib/mysql /etc/mysql  
VOLUME ["$DATA_DIR"]  
WORKDIR ["$DATA_DIR"]  
EXPOSE $PORT1 $PORT2 $PORT3 $PORT4  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mysqld"]  


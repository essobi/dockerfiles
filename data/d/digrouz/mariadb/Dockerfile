FROM centos:7  
LABEL maintainer "DI GREGORIO Nicolas <ndigregorio@ndg-consulting.tech>"  
  
### Environment variables  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
MDB_VERSION='10.2'  
### Install Application  
RUN { \  
echo "[mariadb]"; \  
echo "name = MariaDB"; \  
echo "baseurl = http://yum.mariadb.org/${MDB_VERSION}/centos7-amd64"; \  
echo "gpgcheck=1"; \  
echo "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB"; \  
echo "enabled=1"; \  
} | tee /tmp/MariaDB.repo && \  
yum-config-manager --add-repo /tmp/MariaDB.repo && \  
yum install -y http://www.percona.com/downloads/percona-
release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm && \  
yum update -y && \  
yum install -y MariaDB-server \  
MariaDB-client \  
percona-xtrabackup-24 \  
socat \  
pwgen \  
&& \  
mkdir /docker-entrypoint-initdb.d && \  
rm -rf /var/lib/mysql && \  
mkdir -p /var/lib/mysql /var/run/mysqld && \  
chown -R mysql:mysql /var/lib/mysql /var/run/mysqld && \  
chmod 777 /var/run/mysqld && \  
find /etc/my.cnf.d/ -name '*.cnf' -print0 \  
| xargs -0 grep -lZE '^(bind-address|log)' \  
| xargs -rt -0 sed -Ei 's/^(bind-address|log)/#&/' \  
&& \  
{ \  
echo "[mysqld]"; \  
echo "query_cache_type=0"; \  
echo "innodb_buffer_pool_instances=1"; \  
echo "key_buffer_size=128M"; \  
echo "tmp_table_size=256M"; \  
echo "max_heap_table_size=128M"; \  
echo "skip-innodb_doublewrite"; \  
echo "skip-host-cache"; \  
echo "skip-name-resolve"; \  
} | tee /etc/my.cnf.d/docker.cnf && \  
yum install -y gcc \  
git \  
make \  
&& \  
git clone \--depth 1 https://github.com/ncopa/su-exec /tmp/su-exec && \  
cd /tmp/su-exec && \  
make && \  
cp /tmp/su-exec/su-exec /usr/local/bin/su-exec && \  
yum history -y undo last && \  
yum clean all && \  
rm -rf /tmp/* \  
/var/cache/yum/* \  
/var/tmp/*  
  
# Expose volumes  
VOLUME ["/var/lib/mysql"]  
  
# Expose ports  
EXPOSE 3386  
### Running User: not used, managed by docker-entrypoint.sh  
USER root  
  
### Start postgres  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["mysqld"]  
  


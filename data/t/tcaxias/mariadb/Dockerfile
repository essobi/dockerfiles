# Container for MariaDB 10.1  
FROM tcaxias/debian  
MAINTAINER Tiago Caxias http://github.com/tcaxias  
  
ENV \  
PKGS="percona-xtrabackup-24 mariadb-server-10.1 supervisor filebeat wget pigz
apt-transport-https" \  
DEPS="git golang-1.7-go wget apt-transport-https ca-certificates" \  
GO="/usr/lib/go-1.7/bin/go" \  
GOPATH="/tmp/go" \  
RM_DIRS="/usr/share/doc /usr/share/man /usr/share/info /usr/share/doc-base
/usr/share/systemd /var/lib/apt/lists /var/lib/mysql" \  
RO_SLAVE=1 \  
HEALTH_API_PORT=63306 \  
MASTER_HOST=''  
ADD my.cnf /root/.my.cnf  
  
RUN touch /root/.my.cnf && \  
mkdir -p \  
/etc/mysql/conf.d \  
/run/mysqld \  
/var/run/mysqld/tmp  
  
RUN \  
$APT update && \  
$APT install $DEPS && \  
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db &&
\  
echo 'deb [arch=amd64]
http://lon1.mirrors.digitalocean.com/mariadb/repo/10.1/debian jessie main' \  
> /etc/apt/sources.list.d/mariadb.list && \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 9334A25F8507EFA5 && \  
echo 'deb [arch=amd64] http://repo.percona.com/apt jessie main' \  
> /etc/apt/sources.list.d/percona.list && \  
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
&& \  
echo "deb http://artifacts.elastic.co/packages/5.x/apt stable main" \  
> /etc/apt/sources.list.d/elastic-5.x.list && \  
$APT update && \  
$APT upgrade && \  
$APT install $PKGS && \  
$GO get github.com/hugomcfonseca/mysql_health_api && \  
chmod +x $GOPATH/bin/* && \  
mv $GOPATH/bin/* . && \  
rm -rf $GOPATH && \  
$APT purge $DEPS && \  
$APT install $PKGS && \  
apt-get -yqq autoremove && \  
for i in $RM_DIRS ; do rm -rf $RM_DIRS/* ; done && \  
find / -name "*.a" -exec rm -f {} \;  
  
ADD \  
filebeat.yml \  
/etc/  
  
ADD \  
utils/supervisord.conf \  
utils/mysql_monitor.sh \  
utils/start_mysql.sh \  
/app/  
RUN chmod +x *.sh  
  
# filebeat doesn't get killed by supervisor properly - this is a simple fix  
RUN sed -i -r -e 's#^/usr#exec /usr#' /usr/bin/filebeat.sh  
  
VOLUME [ "/var/lib/mysql", "/var/log/mysql", "/etc/mysql/conf.d",
"/var/run/mysqld" ]  
EXPOSE 3306 63306  
CMD [ "supervisord", "-c", "/app/supervisord.conf", "-j",
"/dev/shm/supervisor.pid", "-l", "/dev/null" ]  


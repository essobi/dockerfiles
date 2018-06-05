# set base os  
FROM linuxserver/baseimage.nginx  
  
MAINTAINER Mark Burford <sparklyballs@gmail.com>, Kode
<kodestar@linuxserver.io>  
  
# set some environment variables for mariadb to give us our paths  
ENV MYSQL_DIR="/config/mysql"  
ENV DATADIR=$MYSQL_DIR/databases  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# set ports  
EXPOSE 443 3306  
# add percona repo  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A && \  
echo 'deb http://repo.percona.com/apt trusty main' >
/etc/apt/sources.list.d/percona.list  
  
# update apt and install packages  
RUN apt-get update && \  
apt-get install \  
percona-server-server-5.6 \  
percona-server-tokudb-5.6 \  
mysqltuner \  
php5-mysql \  
php5-pgsql \  
wget \  
unzip -qy && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
  
# empty /var/lib/mysql as we are using our own data folders  
rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql  
  
# Tweak my.cnf  
RUN sed -ri 's/^(bind-address|skip-networking)/;\1/' /etc/mysql/my.cnf && \  
sed -i s#/var/log/mysql#/config/log/mysql#g /etc/mysql/my.cnf && \  
sed -i -e 's/\\(user.*=\\).*/\1 abc/g' /etc/mysql/my.cnf && \  
sed -i -e "s#\\(datadir.*=\\).*#\1 $DATADIR#g" /etc/mysql/my.cnf  
  
#Adding Custom files  
RUN mkdir -p /defaults  
ADD defaults/ /defaults/  
RUN cp /etc/mysql/my.cnf /defaults/my.cnf  
ADD init/ /etc/my_init.d/  
ADD services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run  
RUN chmod -v +x /etc/my_init.d/*.sh  


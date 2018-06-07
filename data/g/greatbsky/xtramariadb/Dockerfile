FROM greatbsky/crontab  
MAINTAINER architect.bian  
LABEL name="xtramariadb" license="MIT" build-date="20170303"  
  
ENV VERSION 1.0.0  
ENV XTRABACKUP_VERSION 2.4.6  
ENV MARIADB_VERSION 10.1.21  
RUN yum clean all && yum update -y && cd /data/softs && wget -O xtrabackup.rpm
https://www.percona.com/downloads/XtraBackup/Percona-
XtraBackup-$XTRABACKUP_VERSION/binary/redhat/7/x86_64/percona-
xtrabackup-24-$XTRABACKUP_VERSION-2.el7.x86_64.rpm && yum localinstall -y
xtrabackup.rpm && mkdir -p /data/backup/mariadb  
RUN groupadd -r mysql && useradd -r -g mysql mysql && mkdir -p
/data/env/mariadb && cd /data/softs && wget -O mariadb.tar.gz
http://downloads.mariadb.com/MariaDB/mariadb-10.1/yum/rhel/mariadb-$MARIADB_VERSION-
rhel-7-x86_64-rpms.tar && tar -xf mariadb.tar.gz && cd
mariadb-$MARIADB_VERSION-rhel-7-x86_64-rpms && sed -i
"s|https://downloads.mariadb.com/MariaDB/yum/RPM-GPG-KEY-
MariaDB|https://yum.mariadb.org/RPM-GPG-KEY-MariaDB|g" setup_repository &&
./setup_repository && yum install -y MariaDB-server && rm -rf
/data/softs/mariadb-* && cp /var/lib/mysql/* /data/env/mariadb -r && chown -R
mysql:mysql /data/env/mariadb && rm -rf /data/softs/*  
  
VOLUME /data/env/mariadb  
COPY my.conf /etc/my.cnf  
COPY crontab /etc/crontab  
COPY start.sh /data/env/shell/start.sh  
COPY startbackup.sh /data/env/shell/startbackup.sh  
COPY deletebackup.sh /data/env/shell/deletebackup.sh  
COPY fullbackup.sh /data/env/shell/fullbackup.sh  
COPY incrbackup.sh /data/env/shell/incrbackup.sh  
RUN chmod +x /data/env/shell/*.sh  
  
EXPOSE 3306  
CMD /data/env/shell/start.sh  


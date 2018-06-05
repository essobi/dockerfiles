FROM binsix/centos7  
MAINTAINER LiuBin  
LABEL name="mariadb" license="MIT" build-date="20170812"  
  
ENV MARIADB_VERSION 10.1.26  
RUN yum clean all && yum update -y  
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
EXPOSE 3306  
CMD chown -R mysql:mysql /data/env/mariadb && mysqld --user=mysql


#name of container: docker-openemr  
#versison of container: 0.3.1  
#FROM cantara/debian-sid-zulu-jdk8  
FROM quantumobject/docker-baseimage:15.04  
MAINTAINER Angel Rodriguez "angel@quantumobject.com"  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
# add gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
# FATAL ERROR: please install the following Perl modules before executing
/usr/local/mysql/scripts/mysql_install_db:  
# File::Basename  
# File::Copy  
# Sys::Hostname  
# Data::Dumper  
RUN apt-get update && apt-get install -y perl pwgen --no-install-recommends &&
rm -rf /var/lib/apt/lists/*  
  
RUN set -ex; \  
# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-
build@oss.oracle.com>" imported  
key='A4A9406876FCBD3C456770C88C718D3B5072E1F5'; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
gpg --export "$key" > /etc/apt/trusted.gpg.d/mysql.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list > /dev/null  
  
ENV MYSQL_MAJOR 5.6  
ENV MYSQL_VERSION 5.6.35-1debian8  
  
RUN echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-${MYSQL_MAJOR}" >
/etc/apt/sources.list.d/mysql.list  
  
# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't
have an explicit way to disable the mysql_install_db codepath besides having a
database already "configured" (ie, stuff in /var/lib/mysql/mysql)  
# also, we set debconf keys to make APT a little quieter  
RUN { \  
echo mysql-community-server mysql-community-server/data-dir select ''; \  
echo mysql-community-server mysql-community-server/root-pass password ''; \  
echo mysql-community-server mysql-community-server/re-root-pass password ''; \  
echo mysql-community-server mysql-community-server/remove-test-db select
false; \  
} | debconf-set-selections \  
&& apt-get update && apt-get install -y mysql-server="${MYSQL_VERSION}" && rm
-rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld  
  
# comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo '[mysqld]\nskip-host-cache\nskip-name-resolve' >
/etc/mysql/conf.d/docker.cnf  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
  
#add repository and update the container  
#Installation of nesesary package/software for this containers...  
RUN apt-get update && apt-get install -y -q apache2 \  
php5 \  
libapache2-mod-php5 \  
libdate-calc-perl \  
libdbd-mysql-perl \  
libhtml-parser-perl \  
libdbi-perl \  
libwww-mechanize-perl \  
libxml-parser-perl \  
libtiff-tools \  
php5-mysql \  
php5-cli \  
php5-gd \  
php5-xsl \  
php5-curl \  
php5-mcrypt \  
php-soap \  
imagemagick \  
php5-json \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
#General variable definition....  
##startup scripts  
COPY php.ini /etc/php5/apache2/php.ini  
COPY apache2.conf /etc/apache2/apache2.conf  
  
#Pre-config scrip that maybe need to be run one time only when the container
run the first time .. using a flag to don't  
#run it again ... use for conf for service ... when run the first time ...  
RUN mkdir -p /etc/my_init.d  
COPY startup.sh /etc/my_init.d/startup.sh  
RUN chmod +x /etc/my_init.d/startup.sh  
  
# to add apache2 deamon to runit  
RUN mkdir -p /etc/service/apache2 /var/log/apache2 ; sync  
COPY apache2.sh /etc/service/apache2/run  
RUN chmod +x /etc/service/apache2/run \  
&& cp /var/log/cron/config /var/log/apache2/ \  
&& chown -R www-data /var/log/apache2  
  
#pre-config scritp for different service that need to be run when container
image is create  
#maybe include additional software that need to be installed ... with some
service running ... like example mysqld  
COPY pre-conf.sh /sbin/pre-conf  
RUN chmod +x /sbin/pre-conf ; sync \  
&& /bin/bash -c /sbin/pre-conf \  
# && rm /sbin/pre-conf  
  
#backup or keep data integrity ..  
##scritp that can be running from the outside using docker exec tool ...  
RUN mkdir /sbin/backup  
COPY backup.sh /sbin/backup  
RUN chmod +x /sbin/backup  
VOLUME /var/backups  
  
#add files and script that need to be use for this container  
#include conf file relate to service/daemon  
#script to execute after install configuration done ....  
COPY after_install.sh /sbin/after_install  
RUN chmod +x /sbin/after_install  
  
EXPOSE 80  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  


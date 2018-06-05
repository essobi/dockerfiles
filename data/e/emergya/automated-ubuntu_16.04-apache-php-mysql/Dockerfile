FROM ubuntu:16.04  
ENV BUILD_TIMESTAMP 201704051337  
ENV LOCALE en_US.UTF-8  
EXPOSE 80 443 22  
ADD assets/etc/apt /assets/etc/apt  
  
RUN /bin/bash -c 'ln -fs /assets/etc/apt/sources.list /etc/apt/sources.list'
&& /bin/bash -c 'ln -fs /assets/etc/apt/apt.conf.d/99recommends
/etc/apt/apt.conf.d/99recommends'  
  
RUN apt-get update && \  
# base depends  
DEBIAN_FRONTEND=noninteractive apt-get install -y locales net-tools iputils-
ping iproute2 sysstat iotop tcpdump tcpick bwm-ng tree strace screen rsync
inotify-tools socat wget curl \  
openssh-server openssh-client build-essential automake make autoconf
libpcre3-dev software-properties-common supervisor sudo git vim emacs python-
minimal fontconfig ssmtp mailutils \  
bash-completion less unzip\  
# stack services depends  
apache2 apache2-utils mysql-client mysql-server libapache2-mod-php
libapache2-mod-geoip geoip-database \  
# php depends  
php \  
php-bcmath \  
php-cli \  
php-curl \  
php-dba \  
php-dev \  
php-enchant \  
php-gd \  
php-gd \  
php-gmp \  
php-imap \  
php-interbase \  
php-intl \  
php-json \  
php-ldap \  
php-mbstring \  
php-memcache \  
php-mysql \  
php-odbc \  
php-opcache \  
php-pear \  
php-pgsql \  
php-pspell \  
php-pspell \  
php-readline \  
php-recode \  
#php-snmp \  
php-soap \  
php-sqlite3 \  
php-tidy \  
php-xdebug \  
php-xml \  
php-xmlrpc \  
php-zip  
  
RUN locale-gen $LOCALE && update-locale LANG=$LOCALE  
  
## Install Composer  
RUN curl -k -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
# Setup mariadb  
RUN mkdir -p /var/run/mysqld && \  
chown -R mysql: /var/run/mysqld && \  
mv /etc/mysql/my.cnf /etc/mysql/my.cnf.dist && \  
mv /var/lib/mysql /var/lib/mysql.dist  
  
# Setup Apache  
RUN mkdir -p /var/run/apache2 && \  
chown -R www-data: /var/run/apache2 && \  
a2enmod actions alias authz_host deflate dir expires headers mime rewrite ssl
php7.0 proxy proxy_http && \  
mv /etc/apache2/sites-enabled /etc/apache2/sites-enabled.dist  
  
# Setup ssh  
RUN mkdir -p /var/run/sshd  
  
# since this image will not be built as frequently as before,  
# every individual asset inclusion is replaced by the general on-entrypoint-
rsynced one  
ADD assets /assets  
  
VOLUME
["/var/log/apache2","/var/log/supervisor","/var/log/mysql","/var/lib/mysql"]  
ENTRYPOINT ["/assets/bin/entrypoint"]  


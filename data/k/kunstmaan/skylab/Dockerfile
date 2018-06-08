FROM ubuntu:precise  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C  
  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
RUN echo 'deb http://ppa.launchpad.net/ondrej/apache2/ubuntu precise main' >>
/etc/apt/sources.list && \  
apt-get -y -q update && \  
apt-get -y -q install apache2 && \  
a2enmod autoindex deflate expires filter headers include mime rewrite version
setenvif && \  
apt-get -y -q autoremove && \  
apt-get -y -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo 'deb http://ppa.launchpad.net/ondrej/php5-oldstable/ubuntu precise
main' >> /etc/apt/sources.list && \  
apt-get -y -q update && \  
apt-get -y -q install libapache2-mod-php5 php-apc php-pear php5-curl
php5-pgsql php5-intl php5-memcached php5-imagick php5-mysqlnd php5-imap
php5-gd php5-json php5-xmlrpc php5-xsl php5-mcrypt php5-sybase && \  
apt-get -y -q autoremove && \  
apt-get -y -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get -y -q update && \  
apt-get -y -q install wget && \  
wget https://repo.percona.com/apt/percona-release_0.1-3.precise_all.deb && \  
dpkg -i percona-release_0.1-3.precise_all.deb && \  
apt-get -y -q update && \  
apt-get -y -q install percona-server-server-5.6 percona-server-client-5.6
percona-toolkit percona-xtrabackup && \  
apt-get -y -q autoremove && \  
apt-get -y -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN if mysqladmin --user=root --password="" version 2>&1; then rm -f
/var/log/mysql-root-user.done; mysql -uroot -e "UPDATE mysql.user SET Password
= PASSWORD(\"password\") WHERE User = \"root\"; DELETE FROM mysql.user WHERE
User=\"\"; DELETE FROM mysql.user WHERE User=\"root\" AND Host NOT IN
(\"localhost\", \"127.0.0.1\", \"::1\"); DROP DATABASE IF EXISTS test; FLUSH
PRIVILEGES;"; touch /var/log/mysql-root-user.done; fi  
  
RUN apt-get -y -q update && \  
apt-get -y -q install curl && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
apt-get -y -q autoremove && \  
apt-get -y -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo Europe/Brussels > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
RUN echo 'de_DE ISO-8859-1\n\  
de_DE.UTF-8 UTF-8\n\  
de_DE@euro ISO-8859-15\n\  
en_GB ISO-8859-1\n\  
en_GB.ISO-8859-15 ISO-8859-15\n\  
en_US ISO-8859-1\n\  
en_US.ISO-8859-15 ISO-8859-15\n\  
en_US.UTF-8 UTF-8\n\  
fr_FR ISO-8859-1\n\  
fr_FR.UTF-8 UTF-8\n\  
fr_FR@euro ISO-8859-15\n\  
nl_BE ISO-8859-1\n\  
nl_BE.UTF-8 UTF-8\n\  
nl_BE@euro ISO-8859-15\n\  
nl_NL ISO-8859-1\n\  
nl_NL.UTF-8 UTF-8\n\  
nl_NL@euro ISO-8859-15\n'\  
>> /etc/locale.gen && \  
usr/sbin/locale-gen  
  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
  
COPY default.conf /etc/apache2/sites-available/default  
COPY php.ini /etc/php5/apache2/conf.d/  
COPY php.ini /etc/php5/cli/conf.d/  
COPY run.sh run.sh  
  
RUN chmod +x run.sh  
  
EXPOSE 80  
  
CMD ["./run.sh"]  


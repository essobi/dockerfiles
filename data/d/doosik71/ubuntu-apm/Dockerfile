FROM ubuntu:16.04  
MAINTAINER Doosik Kim <doosik71@gmail.com>  
  
LABEL description="Ubuntu 16.04, Apache 2.4, PHP 7.0, MySQL 5.7"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MYSQL_USER=mysql  
ENV MYSQL_DATA_DIR=/var/lib/mysql  
ENV MYSQL_RUN_DIR=/var/run/mysqld  
ENV MYSQL_LOG_DIR=/var/log/mysql  
  
ENV MYSQL_ROOT_PASSWORD=password  
  
ENV HTML_DOC_DIR=/var/www/html  
  
# Preset mysql.  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN mkdir -p $MYSQL_DATA_DIR $MYSQL_RUN_DIR $MYSQL_LOG_DIR && \  
chown -R mysql:mysql $MYSQL_DATA_DIR $MYSQL_RUN_DIR $MYSQL_LOG_DIR && \  
chmod 777 $MYSQL_RUN_DIR  
  
# install OS packages.  
RUN echo "mysql-server mysql-server/root_password password
$MYSQL_ROOT_PASSWORD" | debconf-set-selections && \  
echo "mysql-server mysql-server/root_password_again password
$MYSQL_ROOT_PASSWORD" | debconf-set-selections && \  
apt-get update && \  
apt-get install -y --no-install-recommends apt-utils && \  
apt-get install -y --no-install-recommends \  
mysql-server-5.7 \  
apache2 \  
php7.0 libapache2-mod-php7.0 \  
php7.0-mysql \  
php7.0-curl \  
php7.0-gd \  
php7.0-intl \  
php-pear \  
php-imagick \  
php7.0-imap \  
php7.0-mcrypt \  
php-memcache \  
php7.0-pspell \  
php7.0-recode \  
php7.0-sqlite3 \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-mbstring \  
php-cli \  
php-gettext \  
curl \  
git \  
unzip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/mysql.conf.d/mysqld.cnf &&
\  
echo -e '[mysqld]\nskip-host-cache\nskip-name-resolve' >
/etc/mysql/conf.d/docker.cnf  
  
RUN /usr/bin/mysqld_safe & \  
sleep 10s && \  
echo "GRANT ALL ON *.* TO root@'%' IDENTIFIED BY '$MYSQL_ROOT_PASSWORD' WITH
GRANT OPTION; FLUSH PRIVILEGES" | mysql && \  
killall mysqld && \  
sleep 10s  
  
# rm -rf /var/lib/mysql && \  
#  
# mysqld --initialize-insecure  
#  
# Install extra utils.  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod a+x /usr/local/bin/composer  
  
# Remove default site, configs, and mods not needed.  
WORKDIR /etc/apache2  
  
RUN rm -f \  
conf-enabled/serve-cgi-bin.conf \  
mods-enabled/autoindex.conf \  
mods-enabled/autoindex.load  
  
# Enable additional configs and mods.  
RUN a2enmod rewrite \  
&& a2enmod headers \  
&& a2enmod deflate \  
&& a2enmod env \  
&& a2enmod expires  
  
# Set port and volume.  
EXPOSE 80 3306  
VOLUME ["$HTML_DOC_DIR", "$MYSQL_DATA_DIR"]  
  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
RUN ln -s usr/local/bin/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
# By default, simply start apache.  
CMD ["mysqld"]  
CMD ["/usr/sbin/apache2ctl -D FOREGROUND"]


FROM php:5.6-apache  
  
MAINTAINER Michele Preti <michelepreti@gmail.com> (lelmarir)  
  
ENV MYSQL_USER=mysql \  
MYSQL_DATA_DIR=/var/lib/mysql \  
MYSQL_RUN_DIR=/run/mysqld \  
MYSQL_LOG_DIR=/var/log/mysql \  
DB_USER=tao \  
DB_PASS=tao \  
DB_NAME=tao \  
TAO_AUTOINSTALL=1 \  
TAO_DB_DRIVER=pdo_mysql \  
TAO_DB_NAME=tao \  
TAO_DB_USER=tao \  
TAO_DB_PASSWORD=tao \  
TAO_MODULE_URL=http://192.168.99.100:80  
  
RUN a2enmod rewrite expires  
  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
  
# install required packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends mysql-server && \  
apt-get install -y --no-install-recommends libpng12-dev libjpeg-dev zip unzip
sudo git && \  
apt-get install -y --no-install-recommends openssh-server apache2 supervisor
&& \  
mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor
&& \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf ${MYSQL_DATA_DIR}  
  
# install php extensions  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \  
docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd && \  
docker-php-ext-configure mysql --with-mysql=mysqlnd && \  
docker-php-ext-configure mysqli --with-mysqli=mysqlnd && \  
docker-php-ext-install pdo && \  
docker-php-ext-install pdo_mysql && \  
docker-php-ext-install mysqli && \  
docker-php-ext-install mysql && \  
docker-php-ext-install gd && \  
docker-php-ext-install mbstring && \  
docker-php-ext-install opcache && \  
docker-php-ext-install zip  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
WORKDIR /var/www/html  
  
RUN git clone \--depth 1 https://github.com/oat-sa/package-tao.git . -b
develop && \  
curl -sS https://getcomposer.org/installer | php && \  
php composer.phar install && \  
find / | grep composer\\.phar | xargs -n 1 rm && \  
rm -rf /root/.composer && \  
chown -R www-data:www-data /var/www/html  
  
COPY tao-docker-entrypoint.sh /tao-entrypoint.sh  
COPY mysql-docker-entrypoint.sh /mysql-entrypoint.sh  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN chmod +x /tao-entrypoint.sh \  
&& chmod +x /mysql-entrypoint.sh \  
&& echo "pdo_mysql.default_socket=/var/run/mysqld/mysqld.sock" >>
/usr/local/etc/php/conf.d/docker-php-ext-mysqli.ini \  
&& echo "mysql.default_socket=/var/run/mysqld/mysqld.sock" >>
/usr/local/etc/php/conf.d/docker-php-ext-mysqli.ini \  
&& echo "mysqli.default_socket=/var/run/mysqld/mysqld.sock" >>
/usr/local/etc/php/conf.d/docker-php-ext-mysqli.ini  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]


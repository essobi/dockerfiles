FROM ubuntu:14.04  
RUN apt-get -y update && \  
apt-get -y install software-properties-common && \  
# Use PHP 5.6  
add-apt-repository ppa:ondrej/php5-5.6 && \  
apt-get -y update && \  
apt-get -y --force-yes install \  
curl \  
git \  
make \  
mysql-client \  
nmap \  
php-pear \  
php5-cli \  
php5-common \  
php5-curl \  
php5-dev \  
php5-fpm \  
php5-gd \  
php5-imagick \  
php5-ldap \  
php5-mcrypt \  
php5-memcached \  
php5-mongo \  
php5-mssql \  
php5-mysql \  
php5-oauth \  
php5-odbc \  
php5-readline \  
php5-redis \  
tree \  
unixodbc \  
unixodbc-dev \  
wget  
  
# Install xdebug & xhprof.  
RUN pecl install xdebug xhprof-0.9.4 && \  
find /usr/lib/php5 \  
-name xdebug.so \  
-exec echo "zend_extension={}" \  
> /etc/php5/mods-available/xdebug.ini \; && \  
find /usr/lib/php5 \  
-name xhprof.so \  
-exec echo "extension={}" \  
> /etc/php5/mods-available/xhprof.ini \;  
  
# Composer and Drush.  
RUN mkdir -p /var/www && \  
chown www-data:www-data /var/www && \  
curl -sS https://getcomposer.org/installer | php5 -- --version=1.0.0-alpha11
&& \  
mv composer.phar /usr/local/bin/composer && \  
ln -s /var/www/.composer/vendor/drush/drush/drush /usr/local/bin/drush  
  
USER www-data  
WORKDIR /var/www  
  
RUN composer global require drush/drush:7.* && \  
drush dl registry_rebuild  
  
USER root  
WORKDIR /root  
  
# Free TDS driver for MSSQL access.  
RUN cd /tmp && \  
wget ftp://ftp.freetds.org/pub/freetds/stable/freetds-0.95.tar.gz && \  
tar -xvzf freetds-0.95.tar.gz && \  
cd freetds-0.95 && \  
./configure --prefix=/usr/local && \  
make && \  
make install && \  
cd /tmp && \  
rm -f ftp://ftp.freetds.org/pub/freetds/stable/freetds-0.95.tar.gz && \  
rm -rf freetds-0.95  
  
# Fix permisions.  
# - Make www-data user uid/gid 1000 since this is the uid that boot2docker  
# will use for mounted directories.  
# - Allow www-user to run drush commands.  
# - Allow www-data to login over SSH.  
RUN usermod -u 1000 www-data && \  
groupmod -g 1000 www-data && \  
chown -R root:www-data /root/.composer && \  
usermod -G dialout -s /bin/bash www-data  
  
EXPOSE 9000  
WORKDIR /var/www/html  
  
# Configuration files.  
ADD php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD php.ini /etc/php5/fpm/php.ini  
ADD php-cli.ini /etc/php5/cli/php.ini  
ADD www.conf /etc/php5/fpm/pool.d/www.conf  
ADD entrypoint.sh /entrypoint.sh  
ADD cron-entrypoint.sh /cron-entrypoint.sh  
  
# Ensure log file exists in custom location.  
RUN mkdir -p /var/log/php5-fpm && \  
touch /var/log/php5-fpm/php5-fpm.log && \  
chown www-data:www-data /var/log/php5-fpm/php5-fpm.log  
  
# Entry points.  
RUN chmod u+x /entrypoint.sh && \  
chmod u+x /cron-entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  


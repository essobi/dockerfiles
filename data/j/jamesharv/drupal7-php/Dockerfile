FROM ubuntu:14.04  
RUN apt-get -y update && \  
apt-get -y install \  
curl \  
git \  
make \  
mysql-client \  
nmap \  
php5-cli \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-imagick \  
php5-mcrypt \  
php5-memcached \  
php5-mongo \  
php5-mssql \  
php5-mysql \  
php5-oauth \  
php5-odbc \  
php5-readline \  
php5-redis \  
php5-xdebug \  
php5-xhprof \  
tree \  
unixodbc \  
unixodbc-dev \  
wget  
  
# Composer and Drush.  
RUN curl -sS https://getcomposer.org/installer | php5 --
--version=1.0.0-alpha11 && \  
mv composer.phar /usr/local/bin/composer && \  
composer global require drush/drush:7.* && \  
ln -s $HOME/.composer/vendor/drush/drush/drush /usr/local/bin/drush && \  
drush dl registry_rebuild  
  
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
chmod 755 /root/ && \  
chmod 755 /root/.composer/ && \  
usermod -s /bin/bash www-data  
  
# Configuration files.  
ADD php.ini /etc/php5/fpm/php.ini  
ADD php-cli.ini /etc/php5/cli/php.ini  
ADD www.conf /etc/php5/fpm/pool.d/www.conf  
ADD entrypoint.sh /entrypoint.sh  
ADD cron-entrypoint.sh /cron-entrypoint.sh  
  
# Entry points.  
RUN chmod u+x /entrypoint.sh && \  
chmod u+x /cron-entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  


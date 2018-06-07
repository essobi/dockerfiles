# VERSION 0.2.0  
  
FROM eboraas/apache:squeeze  
  
MAINTAINER Dmitry Vapelnik <dvapelnik@gmail.com>  
  
RUN groupadd -g 1000 donkey && \  
useradd -u 1000 -g 1000 -G sudo donkey && \  
apt-get update && \  
apt-get install -y \  
curl \  
git \  
php-apc \  
php-date \  
php-db \  
php-gettext \  
php-services-json \  
php-soap \  
php-xajax \  
php5 \  
php5-cli \  
php5-common \  
php5-curl \  
php5-gd \  
php5-imagick \  
php5-intl \  
php5-ldap \  
php5-mcrypt \  
php5-memcache \  
php5-memcached \  
php5-mysql \  
php5-pgsql \  
php5-sqlite \  
php5-xdebug \  
php5-xmlrpc \  
sudo \  
&& \  
ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/ && \  
rm -f /etc/php5/conf.d/suhosin.ini && \  
cat /etc/php5/conf.d/xdebug.ini >> /etc/php5/apache2/php.ini && rm -f
/etc/php5/conf.d/xdebug.ini && \  
sed -i 's/export APACHE_RUN_USER=www-data/export APACHE_RUN_USER=donkey/'
/etc/apache2/envvars && \  
sed -i 's/export APACHE_RUN_GROUP=www-data/export APACHE_RUN_GROUP=donkey/'
/etc/apache2/envvars && \  
sed -i 's/html_errors = Off/html_errors = On/' /etc/php5/apache2/php.ini && \  
sed -i 's/implicit_flush = Off/implicit_flush = On/' /etc/php5/apache2/php.ini
&& \  
echo 'donkey ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.6/gosu-$(dpkg --print-
architecture)" && \  
chown root:donkey /usr/local/bin/gosu && \  
chmod +x /usr/local/bin/gosu && \  
chmod +s /usr/local/bin/gosu && \  
apt-get purge -y curl && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY xdebug.addition.ini /etc/php5/apache2/conf.d/xdebug.addition.ini  
COPY start /start  
  
USER donkey  
  
WORKDIR /var/www  
  
EXPOSE 80  
  
CMD ["/usr/local/bin/gosu", "root", "/bin/bash", "/start"]  


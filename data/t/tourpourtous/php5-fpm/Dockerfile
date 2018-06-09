FROM debian:jessie  
  
MAINTAINER Ernesto Baez <ernesto@tourpourtous.com>  
  
# Update system and install required packages  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV PHP_USER php-data  
ENV PHP_USER_UID 4545  
ENV PHP_GROUP php-data  
ENV PHP_GROUP_GID 4545  
ENV XDEBUG_ENABLED 0  
RUN \  
apt-get update && \  
apt-get -y install curl autoconf file g++ gcc libc-dev make pkg-config re2c
wget ca-certificates  
  
RUN \  
echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee
/etc/apt/sources.list.d/newrelic.list && \  
wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add -  
  
RUN \  
apt-get update && \  
apt-get -y install \  
libpcre3 libpcre3-dev librecode0 libsqlite3-0 libxml2 memcached imagemagick
php-net-smtp php-net-sieve \  
php5 php5-cli php5-curl php5-dbg php5-dev php5-fpm php5-gd php5-imagick
php5-intl php5-ldap php-mail-mime php-crypt-gpg \  
php5-mcrypt php5-memcached php5-mysql php-pear php5-redis php5-sqlite
php5-imap php5-xmlrpc php5-xsl newrelic-php5 && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
RUN \  
wget -O /usr/local/bin/apigen http://apigen.org/apigen.phar && chmod +x
/usr/local/bin/apigen && \  
curl -sS https://getcomposer.org/installer | /usr/bin/php -- --install-
dir=/usr/local/bin --filename=composer && \  
pecl install mongo && echo 'extension=mongo.so' > /etc/php5/mods-
available/mongo.ini && \  
pecl install oauth-1.2.3 && echo 'extension=oauth.so' > /etc/php5/mods-
available/oauth.ini && \  
wget -O /usr/local/bin/phpdoc http://phpdoc.org/phpDocumentor.phar && chmod +x
/usr/local/bin/phpdoc && \  
wget -O /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar && chmod
+x /usr/local/bin/phpunit && \  
curl -LsS http://symfony.com/installer > /usr/local/bin/symfony && chmod a+x
/usr/local/bin/symfony && \  
wget -O /usr/local/bin/wp https://raw.githubusercontent.com/wp-cli/builds/gh-
pages/phar/wp-cli.phar && chmod +x /usr/local/bin/wp && \  
mkdir -p /usr/local/share/wordpress && wget -O
/usr/local/share/wordpress/wp_completion https://github.com/wp-cli/wp-
cli/raw/master/utils/wp-completion.bash  
  
RUN \  
rm -rf /etc/php5/fpm/conf.d && ln -s /etc/php5/mods-available
/etc/php5/fpm/conf.d && \  
rm -rf /etc/php5/cli/conf.d && ln -s /etc/php5/mods-available
/etc/php5/cli/conf.d  
  
# forward logs to docker log collector  
RUN ln -sf /dev/stderr /var/log/php5-fpm.log  
  
COPY etc/memcached.conf /etc/memcached.conf  
COPY etc/www.conf /etc/php5/fpm/pool.d/  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN chmod ug+x /entrypoint.sh  
RUN chmod o+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 9000  
CMD ["php5-fpm", "-c", "/etc/php5/fpm", "--fpm-config", "/etc/php5/fpm/php-
fpm.conf", "-F"]  


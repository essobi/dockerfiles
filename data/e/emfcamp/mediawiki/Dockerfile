FROM php:7.0-fpm  
  
RUN apt-get update && \  
apt-get -y install apt-transport-https git curl libmagickwand-6.q16-dev
imagemagick libicu-dev \  
libpq-dev supervisor nginx cron  
  
RUN docker-php-ext-install pgsql intl zip  
RUN pecl install imagick && docker-php-ext-enable imagick  
RUN pecl install apcu && \  
pecl install apcu_bc-1.0.3 && \  
docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini && \  
docker-php-ext-enable apc --ini-name 20-docker-php-ext-apc.ini  
  
ARG MEDIAWIKI_VERSION_MAJOR=1.30  
ARG MEDIAWIKI_VERSION=1.30.0  
RUN curl -s -o /tmp/keys.txt https://www.mediawiki.org/keys/keys.txt && \  
curl -s -o /tmp/mediawiki.tar.gz
https://releases.wikimedia.org/mediawiki/$MEDIAWIKI_VERSION_MAJOR/mediawiki-$MEDIAWIKI_VERSION.tar.gz
&& \  
curl -s -o /tmp/mediawiki.tar.gz.sig
https://releases.wikimedia.org/mediawiki/$MEDIAWIKI_VERSION_MAJOR/mediawiki-$MEDIAWIKI_VERSION.tar.gz.sig
&& \  
gpg --import /tmp/keys.txt && \  
gpg --list-keys --fingerprint --with-colons | sed -E -n -e
's/^fpr:::::::::([0-9A-F]+):$/\1:6:/p' | gpg --import-ownertrust && \  
gpg --verify /tmp/mediawiki.tar.gz.sig /tmp/mediawiki.tar.gz && \  
mkdir -p /var/www/mediawiki/w /data /images /config && \  
tar -xzf /tmp/mediawiki.tar.gz -C /tmp && \  
mv /tmp/mediawiki-$MEDIAWIKI_VERSION/* /var/www/mediawiki/w && \  
rm -rf /tmp/mediawiki.tar.gz /tmp/mediawiki-$MEDIAWIKI_VERSION/ /tmp/keys.txt
&& \  
chown -R www-data:www-data /images && \  
rm -rf /var/www/mediawiki/w/images && \  
ln -s /images /var/www/mediawiki/w/images  
  
RUN curl -s -o /var/www/mediawiki/w/composer.phar
https://getcomposer.org/composer.phar  
COPY config/composer.local.json /var/www/mediawiki/w/composer.local.json  
RUN cd /var/www/mediawiki/w; php ./composer.phar update --no-dev  
  
RUN apt-get clean; rm -r /var/lib/apt/lists/*  
  
COPY config/php-fpm.conf /usr/local/etc/  
COPY config/supervisord.conf /etc/supervisord.conf  
COPY config/nginx.conf /etc/nginx/nginx.conf  
COPY config/crontab /etc/crontab  
  
RUN ln -s /config/LocalSettings.php /var/www/mediawiki/w/LocalSettings.php  
  
VOLUME ["/images", "/config"]  
EXPOSE 80  
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  
CMD []  


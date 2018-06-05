FROM php:7.0-apache  
MAINTAINER Autoize <info@autoize.com> (@autoize)  
  
# Add Debian backports repo and install Let's Encrypt certbot  
RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list; \  
\  
set -ex; \  
apt-get update; \  
apt-get install -y python-certbot-apache -t jessie-backports;  
  
# Install the PHP extensions we need  
RUN apt-get install -y \  
libc-client-dev \  
libicu-dev \  
libkrb5-dev \  
libmcrypt-dev \  
libssl-dev \  
unzip \  
zip \  
# TODO: Consider removing cron and using a dedicated container for it  
cron \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos; \  
docker-php-ext-install imap intl mbstring mcrypt mysqli pdo pdo_mysql zip
opcache  
  
# Set recommended PHP.ini settings  
# See https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN { \  
echo 'date.timezone= America/Chicago'; \  
echo 'memory_limit = 256M'; \  
echo 'upload_max_filesize = 64M'; \  
echo 'post_max_size = 64M'; \  
} > /usr/local/etc/php/conf.d/php.ini  
  
# Enable Apache Rewrite Module  
RUN a2enmod rewrite expires  
  
VOLUME /var/www/html  
  
# Define Mautic version and expected SHA1 signature  
ENV MAUTIC_VERSION 2.8.0  
# ENV MAUTIC_SHA1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
# Download package and extract to web volume  
RUN set -ex; \  
curl -o mautic.zip -SL
https://s3.amazonaws.com/mautic/releases/${MAUTIC_VERSION}.zip; \  
# echo "$MAUTIC_SHA1 *mautic.zip" | sha1sum -c -; \  
mkdir /usr/src/mautic; \  
unzip mautic.zip -d /usr/src/mautic; \  
rm mautic.zip; \  
chown -R www-data:www-data /usr/src/mautic  
  
# Copy init scripts and custom .htaccess  
COPY ["entrypoint.sh", "makeconfig.php", "makedb.php", "/"]  
  
COPY mautic.cron /etc/cron.d/mautic.cron  
  
RUN chmod 644 /etc/cron.d/mautic.cron; \  
touch /var/log/mautic.cron.log; \  
/usr/bin/crontab /etc/cron.d/mautic.cron; \  
chmod 755 /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  


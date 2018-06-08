FROM telusgelp/php:5.6-apache-composer  
  
ENV MEDIAWIKI_VERSION 1.27  
ENV MEDIAWIKI_VERSION_FULL 1.27.3  
ENV MEDIAWIKIL_MD5 7aefefb0bd5ba8d08ed721f91f8b74ce  
  
# Follows mediawiki installation instructions:
https://www.mediawiki.org/wiki/Manual:Running_MediaWiki_on_Debian_or_Ubuntu  
#Install dependencies  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
imagemagick \  
libicu-dev \  
netcat \  
; \  
rm -rf /var/lib/apt/lists/*  
  
# install PHP extensions for mediawiki  
# use enable for extensions installed with pecl -
https://hub.docker.com/_/php/#PECL extensions  
RUN set -ex; \  
\  
pecl install apcu-4.0.11; \  
docker-php-ext-enable apcu; \  
docker-php-ext-install intl mbstring  
  
# install mediawiki  
RUN set -ex; \  
curl -sS
https://releases.wikimedia.org/mediawiki/${MEDIAWIKI_VERSION}/mediawiki-${MEDIAWIKI_VERSION_FULL}.tar.gz
| tar -xvzf - -C /var/www/html; \  
mv /var/www/html/mediawiki-* /var/www/html/wiki; \  
chown -R www-data:www-data /var/www/html/wiki  
  
# set recommended mediawiki PHP configuration  
# see:
https://www.mediawiki.org/wiki/Manual:Running_MediaWiki_on_Debian_or_Ubuntu#Optional:_Configure_PHP  
RUN { \  
echo 'file_uploads = On'; \  
echo 'upload_max_filesize = 20M'; \  
echo 'memory_limit = 128M'; \  
} > /usr/local/etc/php/conf.d/mediawiki-recommended.ini  
  
# Configure Apache  
COPY apache/mediawiki.conf /etc/apache2/conf-enabled/mediawiki.conf  
  
# Set Default directory to mediawiki install  
WORKDIR /var/www/html/wiki  
  
# Configure User File uploads  
# See: https://www.mediawiki.org/wiki/Manual:Configuring_file_uploads  
VOLUME /var/www/html/wiki/images  
  
#make sure proper permissions are set  
RUN chmod 755 /var/www/html/wiki/images  
  
EXPOSE 80 443  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  


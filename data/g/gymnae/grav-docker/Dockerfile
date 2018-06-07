FROM gymnae/webserverbase:latest  
# dockerfile in portion inspired byby evnsio/grav and opsforge/grav-docker  
MAINTAINER gymnae  
LABEL name="grav-docker"  
LABEL version="0.1"  
  
# install the PHP extensions we need  
RUN apk-install \  
php7@community \  
php7-sodium@community \  
php7-yaml@community \  
php7-session@community \  
php7-mbstring@community \  
php7-json@community \  
php7-simplexml@community \  
php7-ctype@community \  
php7-dom@community \  
php7-xml@community \  
php7-zip@community \  
php7-opcache@community \  
php7-apcu@community \  
php7-exif@community  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
echo 'upload_max_filesize=128M'; \  
echo 'post_max_size=128M'; \  
} > /etc/php7/conf.d/opcache-recommended.ini  
  
VOLUME /var/www/html  
  
# Set user to www-data  
RUN mkdir -p /usr/src/grav/  
  
# Install grav into temp locationv  
ENV INSTALL_DIR=/var/www/localhost/htdocs  
ENV SOURCE=/usr/src/grav  
RUN set -ex; \  
cd $SOURCE && \  
wget https://getgrav.org/download/core/grav-admin/latest -P $SOURCE && \  
unzip $SOURCE/latest -d $SOURCE && \  
rm $SOURCE/latest && \  
chown -R nginx:www-data $SOURCE && \  
cd $SOURCE/grav-admin && \  
sudo -u nginx /usr/bin/php bin/gpm install -f -y admin  
  
# make nginx owner of SOURCE again  
RUN chown -R nginx:www-data $SOURCE  
  
# Configure nginx with grav  
WORKDIR grav-admin  
COPY nginx.conf /etc/nginx/  
COPY grav.conf /etc/nginx/sites-enabled/  
  
COPY docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh && \  
chown root:root /docker-entrypoint.sh  
  
EXPOSE 80 443  
ENTRYPOINT ["/docker-entrypoint.sh"]  


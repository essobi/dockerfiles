FROM php:5.6-fpm  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
bzip2 \  
sudo \  
git \  
libfreetype6-dev \  
libpng12-dev \  
libjpeg-dev \  
libmemcached-dev \  
libmcrypt-dev \  
mysql-client \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl install memcache \  
&& docker-php-ext-enable memcache \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr
--with-freetype-dir=/usr \  
&& docker-php-ext-install \  
gd \  
zip \  
mysql \  
pdo_mysql \  
mcrypt \  
mbstring \  
json \  
gettext \  
&& echo "date.timezone = 'UTC'" > /usr/local/etc/php/php.ini \  
&& echo "short_open_tag = 0" >> /usr/local/etc/php/php.ini \  
&& curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
  
ENV INSTALL_PATH=/var/www/html \  
ROUNDCUBE_VERSION=1.2.2 \  
PASSDB_USER=vimbadmin \  
PASSDB_NAME=vimbadmin \  
PASSDB_HOST=mysql  
  
RUN git clone https://github.com/roundcube/roundcubemail.git ${INSTALL_PATH}
&& \  
echo -n | openssl s_client -connect git.kolab.org:443 | sed -ne '/-BEGIN
CERTIFICATE-/,/-END CERTIFICATE-/p'| tee '/usr/local/share/ca-
certificates/git_kolab_org.crt' && \  
update-ca-certificates && \  
cd ${INSTALL_PATH} && \  
git checkout $ROUNDCUBE_VERSION && \  
mv ${INSTALL_PATH}/composer.json-dist ${INSTALL_PATH}/composer.json && \  
composer install --no-dev && \  
rm -rf ${INSTALL_PATH}/.git  
  
COPY config.inc.php ${INSTALL_PATH}/config/config.inc.php  
COPY password.config.inc.php ${INSTALL_PATH}/plugins/password/config.inc.php  
  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
VOLUME /etc/nginx/conf.d  
COPY nginx.conf /etc/nginx/conf.d/roundcube.conf  
  
COPY start.sh /usr/local/bin/start.sh  
CMD ["/usr/local/bin/start.sh"]  
  


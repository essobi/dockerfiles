FROM augustash/alpine-base-s6:1.0.2  
# environment  
ENV COMPOSER_HOME "/.composer"  
ENV APKLIST \  
php7@php \  
php7-bcmath@php \  
php7-dom@php \  
php7-ctype@php \  
php7-curl@php \  
php7-fpm@php \  
php7-gd@php \  
php7-iconv@php \  
php7-intl@php \  
php7-json@php \  
php7-mbstring@php \  
php7-mcrypt@php \  
php7-mysqlnd@php \  
php7-opcache@php \  
php7-openssl@php \  
php7-pdo@php \  
php7-pdo_mysql@php \  
php7-phar@php \  
php7-posix@php \  
php7-redis@php \  
php7-session@php \  
php7-soap@php \  
php7-xml@php \  
php7-xsl@php \  
php7-zip@php \  
php7-zlib \  
zip  
  
# packages & configure  
RUN curl -sS -o /etc/apk/keys/php-alpine.rsa.pub
http://php.codecasts.rocks/php-alpine.rsa.pub && \  
echo "@php http://php.codecasts.rocks/v3.5/php-7.0" >> /etc/apk/repositories
&& \  
apk-install ${APKLIST} && \  
ln -nfs /usr/bin/php7 /usr/bin/php && \  
curl -sS https://getcomposer.org/installer | \  
php -- --no-ansi --install-dir=/usr/local/bin --filename=composer.phar && \  
curl -sS -o /usr/local/bin/n98-magerun2.phar
http://files.magerun.net/n98-magerun2-latest.phar && \  
chmod a+x /usr/local/bin/composer.phar /usr/local/bin/n98-magerun2.phar && \  
mkdir -p "${COMPOSER_HOME}/cache" && \  
chown -R ash:ash "${COMPOSER_HOME}" && \  
rm -rf /etc/php7/php-fpm.d/* && \  
apk-cleanup  
  
# copy root filesystem  
COPY rootfs /  
  
# external  
EXPOSE 9000  
WORKDIR /src  
  
# run s6 supervisor  
ENTRYPOINT ["/init"]  


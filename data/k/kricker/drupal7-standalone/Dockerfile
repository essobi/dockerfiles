FROM drupal:7  
#Install memcached server  
RUN groupadd -r memcache && useradd -r -g memcache memcache && usermod -a -G
memcache root && usermod -a -G www-data root  
ENV MEMCACHED_VERSION 1.5.0  
ENV MEMCACHED_SHA1 e12af93e63c05ab7e89398e4cfd0bfc7b7bff1c5  
ENV MEMCACHED_HOST localhost  
RUN apt-get update && apt-get install -y wget ca-certificates  
RUN set -x \  
\  
&& buildDeps=' \  
dpkg-dev \  
gcc \  
libc6-dev \  
libevent-dev \  
libsasl2-dev \  
make \  
' \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O memcached.tar.gz
"https://memcached.org/files/memcached-$MEMCACHED_VERSION.tar.gz" \  
&& echo "$MEMCACHED_SHA1 memcached.tar.gz" | sha1sum -c - \  
&& mkdir -p /usr/src/memcached \  
&& tar -xzf memcached.tar.gz -C /usr/src/memcached --strip-components=1 \  
&& rm memcached.tar.gz \  
\  
&& cd /usr/src/memcached \  
\  
&& ./configure \  
\--build="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
\--enable-sasl \  
&& make -j "$(nproc)" \  
\  
&& make test 2>/dev/null || echo "There were failing tests!" \  
&& make install \  
\  
&& cd / && rm -rf /usr/src/memcached \  
\  
&& apt-mark manual \  
libevent-2.0-5 \  
libsasl2-2 \  
&& apt-get purge -y --auto-remove $buildDeps \  
\  
&& memcached -u root -V;  
  
# Install memcached php libraries  
RUN apt-get update && apt-get install -y libmemcached-dev libmemcached11
build-essential zlib1g-dev unzip || true; \  
export PHP_EXT_DIR=/usr/src/php/ext && mkdir -p /usr/src/php/ext/memcached ||
true; \  
wget https://codeload.github.com/php-memcached-dev/php-memcached/zip/php7 &&
unzip php7 && mv php-memcached-php7/* /usr/src/php/ext/memcached && mv php-
memcached-php7/.* /usr/src/php/ext/memcached || true; \  
rm php7 && rm -rf php-memcached-php7 && docker-php-ext-install memcached; \  
echo -e "session.save_handler = memcached" >>
/usr/local/etc/php/conf.d/docker-php-ext-memcached.ini; \  
echo -e 'session.save_path = "'${MEMCACHED_HOST}':11211"' >>
/usr/local/etc/php/conf.d/docker-php-ext-memcached.ini;  
  
# Install composer and drush  
WORKDIR /root  
RUN wget -O composer-setup.php
"https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer"  
# RUN curl -s -f -L -o composer-setup.php
https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer
2>/dev/null || echo "There were issues downloading composer installer!"  
RUN php -r " \  
\$signature =
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410';
\  
\$hash = hash('SHA384', file_get_contents('/root/composer-setup.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/root/composer-setup.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}";  
RUN php composer-setup.php && php -r "unlink('composer-setup.php');" \  
&& mv /root/composer.phar /usr/local/bin/composer;  
WORKDIR /root/.composer  
RUN composer global update; exit 0  
RUN composer global require drush/drush:7.*  
RUN composer global update; exit 0  
WORKDIR /var/www/html  
  
# Remove some packages we're not using any longer  
RUN apt-get purge -y --auto-remove wget ca-certificates  
  
ENV DRUPAL_ENVIRONMENT rancher  
ENV DRUPAL_PUBLIC_DIR sites/default/files  
ENV DRUPAL_PRIVATE_DIR sites/default/files/private  
ENV SITEROOT /var/www/html  
ENV NEW_BRANCH false  
ENV GIT_BRANCH rancher-test  
ENV MEMCACHED_SERVER_PORT 11211  
ADD start.sh /start.sh  
RUN chmod 777 /start.sh  
  
EXPOSE 11211 80 443  
CMD ["/start.sh"]  


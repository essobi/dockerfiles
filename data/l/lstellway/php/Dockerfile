FROM php:7.0-fpm-alpine  
  
# Install Dependencies  
RUN apk add --update --no-cache \  
# gd  
freetype-dev libpng-dev libwebp-dev jpeg-dev \  
# mcrypt  
libmcrypt-dev \  
# xsl  
libxslt-dev \  
# intl  
icu-dev \  
# composer  
curl git subversion openssh openssl mercurial tini bash zlib-dev \  
&& docker-php-ext-configure \  
gd --with-png-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-webp-
dir=/usr/include/ --with-freetype-dir=/usr/include/ \  
&& docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) \  
# intl iconv mcrypt gd pdo_mysql zip soap json xsl mbstring simplexml xml
opcache  
gd mcrypt xsl intl pdo_mysql mysqli zip soap opcache  
  
# Install Composer  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.5.2  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer
\  
&& php -r " \  
\$signature =
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& composer --ansi --version --no-interaction \  
&& rm -rf /tmp/* /tmp/.htaccess  
  
# Create entrypoint for custom shell commands  
RUN mkdir /docker-entrypoint-initphp.d  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["php-fpm"]  


# from https://www.drupal.org/requirements/php#drupalversions  
FROM heremias/rphp:0.1.7  
  
# install the PHP extensions we need  
# postgresql-dev is needed for https://bugs.alpinelinux.org/issues/3642  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
coreutils \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
postgresql-dev \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-install -j "$(nproc)" gd mbstring opcache pdo pdo_mysql
pdo_pgsql zip \  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --virtual .drupal-phpexts-rundeps $runDeps \  
&& apk del .build-deps  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
WORKDIR /var/www/html  
  
# https://www.drupal.org/node/3060/release  
ENV DRUPAL_VERSION 8.4.3  
ENV DRUPAL_MD5 55a53cb43284b3d710a2742d458fc1da  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& ln -s /usr/local/bin/composer /usr/bin/composer  
  
RUN /usr/local/bin/composer config -g repos.packagist composer
https://packagist.jp  
RUN /usr/local/bin/composer global require "hirak/prestissimo"  
  
RUN /usr/local/bin/composer global require "drush/drush:8.*" \  
&& ln -s ~/.composer/vendor/bin/drush /usr/local/bin/drush \  
&& /usr/local/bin/drush -y init  
  
RUN curl -fSL
"https://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o
drupal.tar.gz \  
&& echo "${DRUPAL_MD5} *drupal.tar.gz" | md5sum -c - \  
&& tar -xz --strip-components=1 -f drupal.tar.gz \  
&& rm drupal.tar.gz \  
&& chown -R www-data:www-data sites modules themes


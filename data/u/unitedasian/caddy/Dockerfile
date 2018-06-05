FROM php:7-fpm  
  
MAINTAINER Olivier Pichon <op@united-asian.com>  
  
ARG plugins=expires,filemanager,git,locale,minify,realip  
  
ARG timezone='Asia/Hong_Kong'  
ARG memory_limit=-1  
ARG PHP_INI_DIR=/usr/local/etc/php/conf.d  
  
COPY ./etc/php-fpm.d/www.conf /usr/local/etc/php-fpm.d/www.conf  
  
COPY ./etc/conf.d/ /usr/local/etc/php  
  
COPY Caddyfile /etc/Caddyfile  
  
COPY www/index.html /var/www/html/web/  
  
COPY www/index.php /var/www/html/web/  
  
RUN ulimit -n 4096 \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y --force-yes --fix-missing \  
build-essential \  
git \  
libcurl4-gnutls-dev \  
libicu-dev \  
libmcrypt-dev \  
libpng12-dev \  
locales \  
nodejs \  
openssh-client \  
yarn \  
zlib1g-dev \  
&& docker-php-ext-install \  
curl \  
intl \  
mcrypt \  
opcache \  
pdo_mysql \  
zip \  
&& echo "date.timezone="$timezone > $PHP_INI_DIR/conf.d/date_timezone.ini \  
&& echo "memory_limit="$memory_limit > $PHP_INI_DIR/conf.d/memory_limit.ini \  
&& usermod -u 1001 www-data \  
&& chown -R www-data:www-data /var/www \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
https://getcaddy.com \  
| bash -s
http.cgi,http.cors,http.expires,http.filemanager,http.git,http.minify,http.realip
\  
&& chmod 0755 /usr/local/bin/caddy \  
&& /usr/local/bin/caddy -version \  
&& version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENV PATH "/var/www/.composer/vendor/bin:$PATH"  
WORKDIR /var/www/html  
  
EXPOSE 80 443 2015  
ENTRYPOINT ["/usr/local/bin/caddy"]  
  
CMD ["--conf", "/etc/Caddyfile"]  


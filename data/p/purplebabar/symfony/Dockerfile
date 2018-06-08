FROM php:5.6-fpm  
LABEL maintainer="lalung.alexandre@gmail.com"  
  
ENV NGINX_VERSION 1.12.0-1~jessie  
ENV NJS_VERSION 1.12.0.0.1.10-1~jessie  
  
RUN set -ex \  
&& NGINX_GPGKEY=573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62; \  
found=''; \  
for server in \  
ha.pool.sks-keyservers.net \  
hkp://keyserver.ubuntu.com:80 \  
hkp://p80.pool.sks-keyservers.net:80 \  
pgp.mit.edu \  
; do \  
echo "Fetching GPG key $NGINX_GPGKEY from $server"; \  
apt-key adv --keyserver "$server" \--keyserver-options timeout=10 \--recv-keys
"$NGINX_GPGKEY" && found=yes && break; \  
done; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key $NGINX_GPGKEY" &&
exit 1; \  
echo "deb http://nginx.org/packages/debian/ jessie nginx" >
/etc/apt/sources.list.d/nginx.list \  
\  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -qy \  
wget \  
# NGINX  
nginx=${NGINX_VERSION} \  
nginx-module-xslt=${NGINX_VERSION} \  
nginx-module-geoip=${NGINX_VERSION} \  
nginx-module-image-filter=${NGINX_VERSION} \  
nginx-module-njs=${NJS_VERSION} \  
gettext-base \  
# PHP extensions dependencies  
# intl  
libicu-dev \  
# mcrypt  
libmcrypt-dev \  
# gd  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
# supervisor  
supervisor \  
&& rm -rf /var/lib/apt/lists/* \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
# PHP extensions  
RUN set -ex \  
&& pecl install apcu-4.0.8 \  
&& docker-php-ext-enable apcu \  
&& docker-php-ext-configure gd --with-freetype-dir --with-png-dir --with-jpeg-
dir \  
&& docker-php-ext-install -j$(nproc) intl mcrypt  
  
# Frameworks  
RUN set -ex \  
# Symfony  
&& wget -q -O /usr/local/bin/symfony https://symfony.com/installer \  
&& chmod a+x /usr/local/bin/symfony \  
# Composer  
&& wget -q -O /usr/src/composer-installer https://getcomposer.org/installer \  
&& php /usr/src/composer-installer --install-dir /usr/local/bin --filename
composer \  
# Nodejs  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install --no-install-recommends --no-install-
suggests -qy \  
nodejs \  
yarn \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY php.ini /usr/local/etc/php/php.ini  
COPY custom-fpm.conf /usr/local/etc/php-fpm.d/z-custom.conf  
COPY nginx.conf /etc/nginx/conf.d/default.conf  
  
WORKDIR /var/www/symfony  
  
EXPOSE 80  
  
CMD ["supervisord"]


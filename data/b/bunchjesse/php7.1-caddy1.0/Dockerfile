FROM php:7.1-fpm  
  
# Fixes issues with docker exec  
# See https://github.com/dockerfile/mariadb/issues/3  
RUN echo "export TERM=xterm" >> ~/.bashrc  
  
# Configure  
RUN apt-get update \  
&& cd /tmp \  
# Install deps  
&& apt-get install -y \  
supervisor \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libzip-dev \  
libssh2-1-dev \  
libxml2-dev \  
git \  
rubygems \  
# Configure PHP  
&& pecl channel-update pecl.php.net \  
&& pecl install ssh2-1.0 \  
&& docker-php-ext-enable ssh2 \  
&& docker-php-ext-install -j$(nproc) soap iconv mcrypt zip mysqli pdo
pdo_mysql json exif \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
# XDebug  
&& curl -o xdebug-2.5.0.tgz https://xdebug.org/files/xdebug-2.5.0.tgz \  
&& tar -xvzf xdebug-2.5.0.tgz \  
&& cd xdebug-2.5.0 \  
&& phpize \  
&& ./configure \  
&& make \  
&& mv modules/xdebug.so "$(php -r 'echo ini_get("extension_dir");')" \  
# Composer  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer global require "hirak/prestissimo:^0.3" \  
# Caddy  
&& curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/build?os=linux&arch=amd64&features=ratelimit,realip,minify"
\  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
# Node  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get install -y nodejs build-essential \  
&& npm install -g parallelshell \  
# SASS  
&& gem install sass sass-globbing \  
# Cleanup  
&& rm -rf /tmp/* \  
&& apt-get clean  
  
# Create web root  
RUN mkdir -p /web/public  
COPY index.php /web/public/index.php  
RUN chown -R www-data.www-data /web  
  
# Copy configs  
COPY /php-conf.d/* /usr/local/etc/php/conf.d/  
COPY Caddyfile /etc/docker-caddy/Caddyfile  
COPY ./caddy.d /etc/docker-caddy/conf.d  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Environment configuration  
# Override these for easy customization at runtime  
ENV DOCUMENT_ROOT=/web/public \  
XDEBUG_ENABLED=0 \  
XDEBUG_REMOTE_ENABLE=0 \  
XDEBUG_REMOTE_AUTOSTART=0 \  
XDEBUG_REMOTE_CONNECT_BACK=0 \  
XDEBUG_REMOTE_HOST=localhost \  
XDEBUG_IDEKEY=docker \  
XDEBUG_VAR_DISPLAY_MAX_CHILDREN=128 \  
XDEBUG_VAR_DISPLAY_MAX_DATA=512 \  
XDEBUG_VAR_DISPLAY_MAX_DEPTH=5 \  
PHP_OPCACHE_ENABLED=1 \  
PHP_MEMORY_LIMIT=16M \  
PHP_POST_MAX_SIZE=32M \  
PHP_UPLOAD_MAX_FILESIZE=16M \  
PHP_ERROR_REPORTING="E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED" \  
PHP_MAX_INPUT_VARS=2000  
# Run  
COPY /docker-entrypoint.sh /docker-entrypoint.sh  
COPY /docker-entrypoint.d /docker-entrypoint.d  
RUN chmod +x /docker-entrypoint.sh /docker-entrypoint.d/*  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["supervisord"]


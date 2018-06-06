FROM php:7.1-fpm-alpine  
MAINTAINER Daniel Davidson <github.com/da-n>  
  
# Get build arguments  
ARG UID=1501  
ARG GID=1501  
  
# Update and install packages  
RUN set -ex \  
&& echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories \  
&& apk add \--update \--no-cache \  
alpine-sdk \  
autoconf \  
curl \  
curl-dev \  
git \  
nginx \  
postgresql-dev \  
postgresql-libs \  
supervisor \  
tar \  
  
# PHP Extensions  
&& docker-php-ext-install \  
curl \  
mysqli \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
  
# Add user for app  
&& addgroup -g ${GID} app \  
&& adduser -u ${UID} -h /opt/app -H -G app -s /sbin/nologin -D app \  
&& mkdir -p /opt/app \  
  
# Download Composer and sig  
&& curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
  
# Verify we're installing Composer  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php \--no-ansi \--install-dir=/usr/local/bin
\--filename=composer \--snapshot \  
  
# Download latest  
&& git clone https://github.com/fredsted/webhook.site.git /opt/app/ \  
  
# Remove dev packages and clear package cache  
&& apk del \  
alpine-sdk \  
autoconf \  
curl \  
curl-dev \  
git \  
postgresql-libs \  
tar \  
&& rm -rf /var/cache/apk/* \  
  
# Run initial app setup  
&& cd /opt/app/ \  
&& cp .env.example .env \  
&& composer install \  
&& php artisan key:generate \  
&& touch database/database.sqlite \  
&& php artisan migrate \  
&& chown -R app:app /opt/app \  
  
# Empty out tmp dir  
&& rm -rf /tmp/*  
  
# Expose port 9000  
EXPOSE 80  
  
# Copy over required directories and files  
COPY root /  
  
# Make run.sh executable  
RUN chmod +x /usr/local/bin/entrypoint.sh  
# Run  
CMD ["/usr/local/bin/entrypoint.sh"]  


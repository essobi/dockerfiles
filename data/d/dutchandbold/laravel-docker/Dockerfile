FROM php:7.2-fpm  
  
LABEL maintainer="Dylan Lamers <dylan@dutchandbold.com>"  
  
ENV WORKER_SLEEP 3  
ENV WORKER_TRIES 3  
ENV WORKER_TIMEOUT 60  
ENV WORKER_NUMPROCS 0  
ENV NGINX_VERSION 1.10.3-1+deb9u1  
  
WORKDIR /web  
  
# Update package repositories  
RUN apt-get update  
  
# install nginx  
RUN apt-get install -y nginx=$NGINX_VERSION  
  
# Install php dependencies  
RUN apt-get install -y --no-install-recommends \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libicu-dev \  
libxslt-dev \  
locales \  
gettext \  
libxpm-dev \  
libvpx-dev  
  
# Setup locales  
RUN touch /usr/share/locale/locale.alias;  
COPY config/locale.gen /etc/  
RUN locale-gen  
  
# Setup php with extensions  
RUN docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-jpeg-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-xpm-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-vpx-dir=/usr/lib/x86_64-linux-gnu/  
  
RUN docker-php-ext-install gd exif intl xsl json soap dom zip opcache pdo
pdo_mysql  
RUN pecl install mcrypt-1.0.1 xdebug  
RUN docker-php-ext-enable mcrypt xdebug  
  
ENV PHP_MEMORY_LIMIT 128M  
ENV PHP_POST_MAX_SIZE 8M  
ENV PHP_UPLOAD_MAX_FILESIZE 2M  
  
COPY config/php.ini /usr/local/etc/php/  
  
# Install dependencies  
RUN apt-get install -y \  
mcrypt \  
supervisor \  
cron  
  
# Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
  
RUN mkdir -p /var/www/.composer \  
&& chown www-data:www-data /var/www/.composer  
  
# Forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Copy the default index.php into /web  
COPY index.php /web/public/index.php  
  
# Make /web owned by www-data  
RUN chown www-data:www-data /web  
  
# Setup supervisord config  
COPY config/supervisord.conf /config/  
  
# Setup PHP FPM config  
COPY config/php-fpm.conf /config/  
  
# Copy scripts  
COPY scripts /scripts  
  
RUN chown -Rf www-data:www-data /scripts  
  
# Copy tools  
COPY /tools/add-locale /usr/local/bin  
  
# Copy default nginx config  
ENV NGINX_GZIP_ENABLED on  
ENV NGINX_ASSETS_EXPIRE_IN 14d  
ENV NGINX_SERVER_NAME _  
ENV NGINX_LISTEN 80 default_server  
ENV NGINX_SSL off  
ENV NGINX_SSL_CERTIFICATE /config/ssl/fullchain.pem  
ENV NGINX_SSL_CERTIFICATE_KEY /config/ssl/privkey.pem  
ENV NGINX_SSL_PROTOCOLS TLSv1 TLSv1.1 TLSv1.2  
ENV NGINX_SSL_CIPHERS HIGH:!aNULL:!MD5  
  
RUN mkdir /config/ssl  
  
COPY config/nginx-default.conf /config/  
  
# Laravel Scheduler  
RUN echo '* * * * * . /etc/environment; /scripts/laravel-cron.sh >> /dev/null
2>&1' >> /tmp/crontab.tmp \  
&& crontab -u www-data /tmp/crontab.tmp \  
&& rm -rf /tmp/crontab.tmp  
  
# Xdebug setup  
ENV XDEBUG_REMOTE_ENABLE 0  
ENV XDEBUG_REMOTE_HOST localhost  
ENV XDEBUG_REMOTE_AUTOSTART 0  
ENV XDEBUG_REMOTE_PORT 9000  
ENV XDEBUG_PROFILER_ENABLE 0  
ENV XDEBUG_PROFILER_OUTPUT_DIR /web/storage/logs/xdebug/profiler  
  
COPY /config/php-xdebug.ini /tmp/  
RUN cat /tmp/php-xdebug.ini >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& rm /tmp/php-xdebug.ini  
  
RUN mkdir -p /web/storage/logs/xdebug/profiler  
  
# Cleanup build depedencies  
RUN apt-get purge '*-dev' -y  
RUN apt-get autoremove -y  
  
# Expose http and https ports  
EXPOSE 443 80  
# Run supervisor and deploy script  
CMD ["/scripts/boot.sh"]


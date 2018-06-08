FROM php:5.6-fpm  
MAINTAINER scoutm33@ya.ru  
  
# Variables  
ENV TERM=xterm  
ENV NGINX_VERSION 1.10.2-1~jessie  
  
# Packages installation  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 && \  
echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list && \  
apt-get update && apt-get install -y \  
curl \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libxml2-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
libicu-dev \  
g++ \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
supervisor \  
ssmtp \  
cron \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /etc/nginx/conf.d/* \  
&& rm -rf /usr/share/nginx/html/*  
  
RUN echo "Install php-ext..." \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install pcntl \  
&& docker-php-ext-configure intl && docker-php-ext-install intl \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install zip  
  
# Nginx logs to Docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Configurations files  
COPY conf/php-fpm.d/www.conf /usr/local/etc/php-fpm.d/www.conf  
COPY conf/php-fpm.d/zz-docker.conf /usr/local/etc/php-fpm.d/zz-docker.conf  
COPY conf/php.ini /usr/local/etc/php/conf.d/php-override.ini  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
COPY conf/supervisord.conf /etc/supervisord.conf  
COPY conf/cronjobs /etc/cron.d/php-app-cronjob  
COPY conf/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
# If you add an entry to /etc/cron.d to define a system cronjob you must
ensure that the file has permissions 0644, otherwise the script will not run  
RUN chmod 644 /etc/cron.d/php-app-cronjob  
  
# Application  
COPY . /srv/www/php-app  
  
# fix permissions  
RUN chown -R www-data:www-data /srv/www/php-app/  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  


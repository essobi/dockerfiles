FROM php:7.1-fpm  
MAINTAINER Loïc Ambrosini <loic@1001pharmacies.com>  
  
ENV TERM=xterm  
ENV NGINX_VERSION 1.11.7-1~jessie  
  
ENV BUILD_PKGS \  
libmagickwand-dev \  
libmagickcore-dev \  
libcurl4-gnutls-dev \  
zlib1g-dev \  
libicu-dev  
  
RUN apt-get update && apt-get install --no-install-recommends --no-install-
suggests -y \  
$BUILD_PKGS \  
supervisor \  
git \  
curl \  
make \  
awscli  
  
## Nginx  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base  
  
RUN pecl install \  
imagick \  
xdebug  
  
RUN docker-php-ext-install \  
pdo_mysql \  
intl \  
bcmath \  
zip  
  
RUN docker-php-ext-enable \  
opcache \  
imagick \  
xdebug  
  
COPY docker/php.ini /usr/local/etc/php/  
COPY docker/00-supervisor.conf /etc/supervisor/conf.d/  
  
#Configure xdebug.  
RUN sed -i '1 a xdebug.remote_autostart=true'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_connect_back=1'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN sed -i '1 a xdebug.max_nesting_level = 1200'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer global require hirak/prestissimo \  
&& rm -rf /tmp/* /var/tmp/*  
  
RUN echo Europe/Paris > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
RUN chmod -R g+rwx /var/www/html  
RUN umask 0007  
  
EXPOSE 80 443  
CMD ["supervisord"]


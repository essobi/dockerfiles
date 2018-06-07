FROM php:5.6-fpm  
MAINTAINER Kevin Smith <kevin@kevinsmith.io>  
  
#  
# s6 overlay init and process supervisor  
#  
  
ENV S6_VERSION v1.19.1.1  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz
/tmp/s6-overlay-amd64.tar.gz  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-
amd64.tar.gz.sig /tmp/s6-overlay-amd64.tar.gz.sig  
RUN \  
# Verify GPG signature - "Just Containers <just-containers@jrjrtech.com>"  
curl https://keybase.io/justcontainers/key.asc | gpg --import \  
&& gpg --verify /tmp/s6-overlay-amd64.tar.gz.sig /tmp/s6-overlay-amd64.tar.gz
\  
  
# Install  
&& tar xvfz /tmp/s6-overlay-amd64.tar.gz -C / && rm /tmp/s6-overlay-
amd64.tar.gz  
  
  
#  
# Additional PHP extensions and configuration  
#  
# Install GD extension  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
  
&& docker-php-ext-configure gd --with-freetype-dir=/usr --with-png-dir=/usr
\--with-jpeg-dir=/usr \  
&& docker-php-ext-install -j$(nproc) gd \  
  
# Install ImageMagick extension  
&& apt-get install -y --no-install-recommends \  
libmagickwand-6.q16-dev \  
  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin/ \  
&& pecl install imagick \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
  
# Install Phpredis  
&& pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini \  
  
# Install other Docker extensions  
&& docker-php-ext-install -j$(nproc) \  
mysqli \  
mcrypt \  
opcache \  
pdo_mysql \  
sockets \  
  
# Cleanup  
&& apt-get purge -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmagickwand-6.q16-dev \  
&& rm -rf /var/lib/apt/lists/*  
# Custom php config  
COPY php/php-fpm.conf /usr/local/etc/php-fpm.d/zzz-custom.conf  
COPY php/php.ini /usr/local/etc/php/  
  
  
#  
# Install and configure nginx  
#  
  
ENV NGINX_VERSION 1.13.3-1~jessie  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update && apt-get install -y --no-install-recommends --no-install-
suggests \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
  
# Cleanup  
&& rm -rf /var/lib/apt/lists/*  
# Send logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN mkdir -p /etc/nginx/ssl/ \  
&& openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048  
  
EXPOSE 80 443  
# Install j2cli for nginx config file templates  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-dev \  
python-setuptools \  
  
&& easy_install j2cli \  
  
# Cleanup  
&& apt-get purge -y \  
python-dev \  
python-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
# Custom nginx config  
COPY nginx /etc/nginx/imported  
RUN cp /etc/nginx/imported/nginx.conf /etc/nginx/nginx.conf \  
&& cp /etc/nginx/imported/certs/self-signed.crt /etc/nginx/ssl/self-signed.crt
\  
&& cp /etc/nginx/imported/certs/self-signed.key /etc/nginx/ssl/self-signed.key  
  
ADD html /var/www/html  
  
  
ADD services.d /etc/services.d/  
  
ENTRYPOINT ["/init"]  


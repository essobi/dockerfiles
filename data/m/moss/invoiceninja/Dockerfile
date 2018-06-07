FROM php:7-fpm  
  
MAINTAINER Thiago Almeida <thiagoalmeidasa@gmail.com>  
  
  
#####  
# SYSTEM REQUIREMENT  
#####  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libmcrypt-dev zlib1g-dev git libgmp-dev \  
libfreetype6-dev libjpeg62-turbo-dev libpng12-dev nginx \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/ \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-configure gmp \  
&& docker-php-ext-install iconv mcrypt mbstring pdo pdo_mysql zip gd gmp \  
&& rm -rf /var/lib/apt/lists/*  
  
#####  
# INSTALL COMPOSER  
#####  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/local/bin --filename=composer  
  
#####  
# DOWNLOAD AND INSTALL INVOICE NINJA  
#####  
ENV INVOICENINJA_VERSION 2.8.1  
RUN curl -SL https://github.com/hillelcoren/invoice-
ninja/archive/v${INVOICENINJA_VERSION}.tar.gz \  
| tar -xz -C /var/www/ \  
&& mv /var/www/invoiceninja-${INVOICENINJA_VERSION} /var/www/app \  
&& composer install --working-dir /var/www/app -o --no-dev --no-interaction \  
\--no-progress  
RUN mv /var/www/app/storage /var/www/app/docker-backup-storage \  
&& mv /var/www/app/public/logo /var/www/app/docker-backup-public-logo \  
&& chown -R www-data:www-data /var/www/app/  
  
######  
# DEFAULT ENV  
######  
ENV DB_HOST mysql  
ENV DB_DATABASE ninja  
ENV APP_KEY SomeRandomStringSomeRandomString  
ENV LOG errorlog  
ENV APP_DEBUG 0  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# NginX Configuration  
ADD nginx.conf /etc/nginx/nginx.conf  
  
#Use to persist with your files upload  
VOLUME /var/www/app/storage  
VOLUME /var/www/app/public/logo  
  
WORKDIR /var/www/app  
  
EXPOSE 80  
COPY app-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  


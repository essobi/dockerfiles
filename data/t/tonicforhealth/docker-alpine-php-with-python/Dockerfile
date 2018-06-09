FROM php:5.5.38-alpine  
  
ENV PHPREDIS_VERSION 2.2.5  
# PHP env  
RUN docker-php-ext-install bcmath pcntl && \  
curl -sS https://getcomposer.org/installer \  
| php -- --install-dir=/usr/local/bin --filename=composer && \  
echo "date.timezone = \"UTC\"" >/usr/local/etc/php/conf.d/timezone.ini  
  
# ENV for the functional tests  
RUN apk add --no-cache \  
git \  
python \  
bash \  
mariadb-client \  
ncurses  
  
# install and enable php redis extension  
RUN curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& [ -d /usr/src/php/ext ] || mkdir -p /usr/src/php/ext \  
&& mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& docker-php-ext-install pdo pdo_mysql redis  
  


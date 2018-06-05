FROM php:7-fpm-alpine  
  
MAINTAINER Tien Nhan <nhantien.ca@gmail.com>  
  
ENV TERM xterm  
  
WORKDIR /var/www/html  
  
RUN apk add --no-cache --virtual build-dependencies  
  
# install neccesary package  
RUN apk add --update --no-cache alpine-sdk bash autoconf curl freetype-dev gdb
git htop icu-dev \  
libmcrypt-dev libtool libltdl libjpeg-turbo-dev libpng-dev \  
make re2c strace tzdata zip pcre-dev libxml2-dev pwgen linux-headers  
  
# install stack component  
RUN apk add --update --no-cache supervisor nginx varnish redis  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# install wp-cli  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
# install and configure some php extension  
RUN pecl install -f redis-3.1.4  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ --with-png-dir=/usr/include/ \  
&& docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) gd intl mysqli
pdo_mysql zip bcmath mcrypt exif soap \  
&& docker-php-ext-enable opcache redis  
  
RUN wget http://download.redis.io/redis-stable.tar.gz \  
&& tar xvzf redis-stable.tar.gz \  
&& cd redis-stable  
  
# Credit: https://github.com/docker-library/redis  
# disable Redis protected mode [1] as it is unnecessary in context of Docker  
# (ports are not automatically exposed when running inside Docker, but rather
explicitly by specifying -p / -P)  
# [1]:
https://github.com/antirez/redis/commit/edd4d555df57dc84265fdfb4ef59a4678832f6da  
RUN grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 1$' redis-
stable/src/server.h; \  
sed -ri 's!^(#define CONFIG_DEFAULT_PROTECTED_MODE) 1$!\1 0!' redis-
stable/src/server.h; \  
grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 0$' redis-stable/src/server.h;  
  
RUN make -C redis-stable -j "$(nproc)"; \  
make -C redis-stable install; \  
rm -rf redis-stable \  
apk del build-dependencies  
  
RUN mkdir -p /etc/nginx/sites-available/ \  
&& mkdir -p /etc/nginx/sites-enabled/ \  
&& mkdir -p /etc/nginx/ssl/ \  
&& mkdir -p /var/www/app \  
&& mkdir -p /run/nginx \  
&& mkdir -p /var/run/redis/ \  
&& mkdir -p /var/log/redis/ \  
&& mkdir -p /etc/redis \  
&& mkdir -p /var/log/supervisor  
  
COPY conf/app.ini /usr/local/etc/php/conf.d/  
  
COPY conf/supervisord.conf /etc/supervisord.conf  
  
COPY conf/varnish-default.vcl /etc/varnish/default.vcl  
  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
  
COPY conf/nginx-site.conf /etc/nginx/sites-available/default.conf  
  
COPY conf/redis.conf /etc/redis/redis.conf  
  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
RUN composer create-project roots/bedrock app  
  
RUN echo "define('WP_CACHE_KEY_SALT', env('WP_CACHE_KEY_SALT'));" >>
app/config/application.php  
  
WORKDIR /var/www/html/app  
  
COPY conf/object-cache.php web/app/object-cache.php  
  
RUN chown -R www-data:www-data web/app/uploads  
  
COPY docker-entrypoint.sh /  
  
RUN chmod 755 /docker-entrypoint.sh  
  
CMD ["/docker-entrypoint.sh"]  


FROM php:7-fpm  
  
RUN apt-get update && apt-get install -y \  
git \  
build-essential \  
libssl-dev  
  
# Compile Data Structures extension  
RUN git clone https://github.com/php-ds/extension "php-ds" \  
&& cd php-ds \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& docker-php-ext-enable ds  
  
# Compile Redis extension  
RUN git clone \--branch php7 https://github.com/phpredis/phpredis "php-redis"
\  
&& cd php-redis \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& docker-php-ext-enable redis  
  
RUN apt-get install -y libmemcached-dev \  
&& git clone \--branch php7 https://github.com/php-memcached-dev/php-memcached
"memcached" \  
&& cd memcached \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& docker-php-ext-enable memcached  
  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
  
RUN apt-get install -y librabbitmq-dev \  
&& pecl install amqp && docker-php-ext-enable amqp  
  
RUN apt-get install -y curl libcurl4-openssl-dev \  
&& docker-php-ext-install curl  
  
RUN docker-php-ext-install pdo_mysql  
  
RUN apt-get install -y libicu-dev \  
&& docker-php-ext-install intl  
  
RUN docker-php-ext-install bcmath && \  
docker-php-ext-install mbstring && \  
docker-php-ext-install zip  
  
RUN apt-get install -y libmcrypt-dev \  
&& docker-php-ext-install mcrypt  
  
RUN apt-get install -y libxml2-dev \  
&& docker-php-ext-install soap  
  
# tweak php-fpm config  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /usr/local/etc/php-
fpm.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 1000/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/;pm.status_path = \/status/pm.status_path = \/status/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/;ping.path = \/ping/ping.path = \/ping/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/;ping.response = pong/ping.response = pong/g" /usr/local/etc/php-
fpm.d/www.conf  
  
RUN echo "xdebug.var_display_max_depth = 5" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN echo "xdebug.var_display_max_children = 256" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN echo "xdebug.var_display_max_data = 1024" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  


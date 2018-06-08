FROM php:7.0.11-fpm  
  
ENV MAKEFLAGS="-j$[$(nproc) + 1]" \  
SRC=/usr/local/src  
  
WORKDIR /var/www/public  
  
RUN apt-get update && apt-get install -y git build-essential libssl-dev --no-
install-recommends && \  
# Compile Memcached extension  
apt-get install -y libmemcached-dev --no-install-recommends && \  
cd ${SRC} && git clone --branch php7 https://github.com/php-memcached-dev/php-
memcached "memcached" && \  
cd memcached && \  
phpize && \  
./configure && \  
make && \  
make install && \  
make clean && \  
docker-php-ext-enable memcached && \  
# Compile igbinary extension  
cd ${SRC} && git clone https://github.com/igbinary/igbinary "php-igbinary" &&
\  
cd php-igbinary && \  
phpize && \  
./configure && \  
make && \  
make install && \  
make clean && \  
docker-php-ext-enable igbinary && \  
# Compile Redis extension  
cd ${SRC} && git clone --branch php7 https://github.com/phpredis/phpredis
"php-redis" && \  
cd php-redis && \  
phpize && \  
./configure --enable-redis-igbinary && \  
make && \  
make install && \  
make clean && \  
docker-php-ext-enable redis && \  
# curl extension  
apt-get install -y curl libcurl4-openssl-dev --no-install-recommends && \  
docker-php-ext-install curl && \  
# pdo_mysql extension  
docker-php-ext-install pdo_mysql && \  
# intl extension  
apt-get install -y libicu-dev --no-install-recommends && \  
docker-php-ext-install intl && \  
# mcrypt extension  
apt-get install -y libmcrypt-dev --no-install-recommends && \  
docker-php-ext-install mcrypt && \  
# bcmath, mbstring and zip extensions  
docker-php-ext-install bcmath && \  
docker-php-ext-install mbstring && \  
docker-php-ext-install zip && \  
# data structures extension  
pecl install ds && \  
docker-php-ext-enable ds && \  
# amqp extension  
apt-get install -y librabbitmq-dev --no-install-recommends && \  
pecl install amqp && \  
docker-php-ext-enable amqp && \  
# soap extension  
apt-get install -y libxml2-dev --no-install-recommends && \  
docker-php-ext-install soap && \  
# xdebug extension  
pecl install xdebug && \  
docker-php-ext-enable xdebug && \  
# clean  
apt-get purge -qy --auto-remove git build-essential libssl-dev && \  
apt-get autoclean -qy && rm -rf /var/lib/apt/lists && \  
rm -rf ${SRC}  
  
# copy original php.ini configuration  
ADD php.ini /usr/local/etc/php/php.ini  
  
# tweak php.ini configuration  
RUN sed -i -e "s/expose_php = On/expose_php = Off/g"
/usr/local/etc/php/php.ini && \  
sed -i -e "s/;\?\\(date.timezone =\\).*/\1 Europe\/London/g"
/usr/local/etc/php/php.ini && \  
sed -i -e "s/session.serialize_handler = .*$/session.serialize_handler =
igbinary/g" /usr/local/etc/php/php.ini && \  
# tweak php-fpm config http://myshell.co.uk/blog/2012/07/adjusting-child-
processes-for-php-fpm-nginx/  
# /usr/local/etc/php-fpm.d  
sed -i -e "s/pm.max_children = 5/pm.max_children = 50/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 15/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 10/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 20/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/;pm.max_requests = 500/pm.max_requests = 1000/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/;pm.status_path = \/status/pm.status_path = \/status/g"
/usr/local/etc/php-fpm.d/www.conf && \  
sed -i -e "s/;ping.path = \/ping/ping.path = \/ping/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/;ping.response = pong/ping.response = pong/g" /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e "s/\\(access.log = .*\\)/;\1/" /usr/local/etc/php-fpm.d/docker.conf
&& \  
# tweak xdebug extension  
echo "xdebug.var_display_max_depth = 5" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini && \  
echo "xdebug.var_display_max_children = 256" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \  
echo "xdebug.var_display_max_data = 1024" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
  


FROM wodby/drupal-php:7.1  
  
USER root  
  
ENV PHP_URL="https://secure.php.net/get/php-7.1.13.tar.xz/from/this/mirror"  
  
RUN set -ex; \  
\  
git clone https://github.com/longxinH/xhprof; \  
\  
apk add --no-cache \  
libxml2-dev \  
php7-dev \  
php7-xml \  
autoconf \  
make \  
gcc \  
g++ \  
re2c \  
curl \  
file; \  
\  
cd xhprof/extension; \  
\  
phpize; \  
\  
./configure; \  
\  
sudo make && sudo make install; \  
\  
mkdir -p /usr/src; \  
cd /usr/src; \  
\  
wget -O php.tar.xz "$PHP_URL"; \  
\  
docker-php-ext-install \  
simplexml \  
xml; \  
\  
docker-php-ext-enable \  
simplexml \  
xml \  
xhprof; \  
\  
curl https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar -o
/usr/local/bin/phpcs.phar; \  
\  
chmod +x /usr/local/bin/phpcs.phar; \  
\  
ln -s /usr/local/bin/phpcs.phar /usr/local/bin/phpcs; \  
\  
apk del --purge \  
libxml2-dev \  
php7-dev \  
php7-xml \  
autoconf \  
make \  
gcc \  
g++ \  
re2c \  
curl \  
file  
  
  
USER www-data  


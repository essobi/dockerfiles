ARG BASE=php:7.1-alpine  
FROM ${BASE}  
  
RUN apk --no-cache add autoconf gcc g++ make &&\  
pecl install xdebug &&\  
rm -fr /tmp/pear  
  
RUN docker-php-ext-enable xdebug  
  
RUN docker-php-source extract &&\  
mkdir -p /usr/src/php/ext/ast &&\  
curl -fsSL https://github.com/nikic/php-ast/archive/v0.1.5.tar.gz |\  
tar xzf - --strip-components=1 -C /usr/src/php/ext/ast &&\  
docker-php-ext-install ast &&\  
docker-php-source delete  
  
RUN docker-php-ext-install pdo_mysql pcntl  
  
RUN apk --no-cache add libpng-dev &&\  
docker-php-ext-install gd  
  
RUN apk --no-cache add zlib-dev &&\  
docker-php-ext-install zip  
  
RUN apk --no-cache add git mysql-client  
  
RUN docker-php-ext-enable opcache  
  
ADD https://phar.phpunit.de/phpunit.phar /usr/local/bin/phpunit  
ADD https://getcomposer.org/composer.phar /usr/local/bin/composer  
ADD http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar /usr/local/bin/php-
cs-fixer  
  
RUN chmod +x /usr/local/bin/phpunit &&\  
chmod +x /usr/local/bin/composer &&\  
chmod +x /usr/local/bin/php-cs-fixer  
  
RUN composer create-project etsy/phan /tmp/phan --prefer-dist --no-dev &&\  
cd /tmp/phan &&\  
mkdir -p build &&\  
php -d phar.readonly=0 package.php &&\  
install -m755 build/phan.phar /usr/local/bin/phan &&\  
rm -fr /tmp/phan


FROM php:7.0.9-cli  
  
MAINTAINER Baptiste Gaillard <baptiste.gaillard@gomoob.com>  
  
ENV COMPOSER_VERSION 1.2.0  
ENV PHP_WEBSOCKET_SERVER_VERSION 1.0.3  
# Install useful packages  
RUN apt-get update  
RUN apt-get install -y zip wget  
  
# Install Composer  
# see https://github.com/RobLoach/docker-composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php  
  
# Install the server  
WORKDIR /home  
RUN wget https://github.com/gomoob/php-websocket-
server/archive/$PHP_WEBSOCKET_SERVER_VERSION.tar.gz  
RUN tar -zxvf $PHP_WEBSOCKET_SERVER_VERSION.tar.gz  
  
# Install composer dependencies  
WORKDIR /home/php-websocket-server-$PHP_WEBSOCKET_SERVER_VERSION  
RUN composer update --prefer-dist --no-dev --optimize-autoloader --prefer-
stable  
  
COPY bin/server.php /home/php-websocket-server-$PHP_WEBSOCKET_SERVER_VERSION  
COPY conf/auth.yml /etc/auth.yml  
  
# The default command is php  
CMD php ./server.php  


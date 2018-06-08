FROM php:7.1-fpm  
ARG TIMEZONE  
ARG PHP_VERSION  
ARG INSTALL_SYMPHONY  
ARG SYMPHONY_VERSION  
  
MAINTAINER Maxence POUTORD <maxence.poutord@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
openssl \  
git  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
# Set timezone  
RUN ln -snf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && echo ${TIMEZONE}
> /etc/timezone  
RUN printf '[PHP]\ndate.timezone = "%s"\n', ${TIMEZONE} >
/usr/local/etc/php/conf.d/tzone.ini  
RUN "date"  
  
# Type docker-php-ext-install to see available extensions  
RUN docker-php-ext-install pdo pdo_mysql  
RUN apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip  
  
# install xdebug  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
RUN echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
RUN echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini  
RUN echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini  
RUN echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
RUN echo "xdebug.idekey=\"xdebug\"" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
  
RUN echo 'alias sf="php app/console"' >> ~/.bashrc  
RUN echo 'alias sf3="php bin/console"' >> ~/.bashrc  
RUN echo 'alias phpunit="php bin/simple-phpunit"' >> ~/.bashrc  
  
WORKDIR /var/www/symfony  
  
EXPOSE 9001


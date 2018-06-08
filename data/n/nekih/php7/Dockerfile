FROM php:7.1.4-fpm  
  
RUN apt-get update && apt-get install -y \  
git \  
unzip \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libpcre3-dev \  
libicu52 \  
&& rm -rf /var/lib/apt/lists/*  
RUN docker-php-ext-install intl \  
&& docker-php-ext-install pdo_mysql \  
# && docker-php-ext-install pdo \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
# && docker-php-ext-install iconv \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install exif \  
&& docker-php-ext-install opcache \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && composer --version  
RUN mkdir -p /usr/local/bin && curl -LsS https://symfony.com/installer -o
/usr/local/bin/symfony && chmod a+x /usr/local/bin/symfony  
  
# Set timezone  
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime
&& "date"  
  
RUN echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo 'alias sf="php app/console"' >> ~/.bashrc  
RUN echo 'alias sf3="php bin/console"' >> ~/.bashrc  
  
COPY php.ini /usr/local/etc/php/conf.d/  
COPY default.conf /usr/local/etc/php-fpm.d/www.conf  
  
RUN mkdir -p /var/www/.composer \  
&& composer global require hirak/prestissimo  
  
RUN chown -R www-data:www-data /var/www  
  
RUN usermod -u 1000 www-data  
#RUN adduser -D -g '' -G www-data www-data  
USER 1000  
VOLUME ["/var/www/symfony"]  
  
WORKDIR /var/www/symfony  


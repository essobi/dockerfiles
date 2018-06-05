FROM php:7.1-apache  
  
# System packages  
RUN apt-get update -qq \  
&& apt-get install -y unzip git-core libicu-dev vim-tiny ssh \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apk/*  
  
# Apache configuration  
RUN a2enmod rewrite \  
&& a2enmod ssl \  
&& a2dissite 000-default \  
&& echo ServerName localhost >> /etc/apache2/apache2.conf  
  
COPY config/vhost/* /etc/apache2/sites-available/  
COPY config/php.ini /usr/local/etc/php/  
  
RUN a2ensite symfony  
  
# Install PHP extensions  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-install bcmath intl sockets opcache pdo_mysql \  
&& pecl install apcu-5.1.8 \  
&& docker-php-ext-enable apcu  
  
# Enable remote debugging with xdebug  
RUN echo 'xdebug.remote_enable=on' >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo 'xdebug.remote_connect_back=on' >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo 'xdebug.remote_autostart=on' >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer global require hirak/prestissimo


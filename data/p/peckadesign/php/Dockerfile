FROM php:5.5-apache  
  
RUN pecl install redis && docker-php-ext-enable redis  
RUN pecl install xdebug-2.5.5  
RUN docker-php-ext-install \  
pdo \  
pdo_mysql \  
opcache \  
bcmath \  
calendar  
  
RUN a2enmod rewrite  
RUN apt-get update -y \  
&& apt-get install -y \  
libxml2-dev \  
git \  
zlib1g-dev \  
libpng-dev \  
libmagickwand-dev \  
&& apt-get clean -y  
  
RUN yes | pecl install imagick  
RUN docker-php-ext-enable imagick  
  
RUN docker-php-ext-install soap zip gd  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN mkdir /root/.ssh && ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
RUN composer global require hirak/prestissimo  


FROM php:7.1.1-apache  
MAINTAINER phonoloop <phonoloop@spaceape.be>  
  
# Update  
RUN apt-get update  
  
# VHOST change  
COPY ./vhost.conf /etc/apache2/sites-available/vhost.conf  
RUN a2dissite 000-default.conf \  
&& a2ensite vhost.conf  
  
# Enable Apache modules  
RUN a2enmod rewrite  
RUN a2enmod ssl  
  
# Download extension dependencies  
RUN apt-get install -y \  
libcurl3-dev \  
libxml2-dev \  
libzzip-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libicu-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure extension  
RUN docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/  
  
# Install extensions  
RUN docker-php-ext-install curl \  
&& docker-php-ext-install xml \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install intl  
  
# opcache  
RUN docker-php-ext-install opcache  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
RUN echo "realpath_cache_size = 4096k; realpath_cache_ttl = 7200;" >
/usr/local/etc/php/conf.d/php.ini  
  
# Install Composer  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install Xdebug  
RUN pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug


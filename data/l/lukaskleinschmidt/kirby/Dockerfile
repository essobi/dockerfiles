FROM php:7.1-apache  
  
COPY config/php.ini /usr/local/etc/php/  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libjpeg-dev \  
libpng12-dev \  
libmagickwand-dev \  
imagemagick \  
git \  
zip \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install exif \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install imagick  
RUN pecl install imagick \  
&& docker-php-ext-enable imagick  
  
# Install composer and Kirby CLI  
RUN curl --silent --show-error https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
ENV PATH "$PATH:~/.composer/vendor/bin"  
# Install go  
RUN curl -O https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz \  
&& tar -xvf go1.9.linux-amd64.tar.gz \  
&& mv go /usr/local  
  
ENV PATH "$PATH:/usr/local/go/bin"  
# Install mhsendmail  
RUN go get github.com/mailhog/mhsendmail \  
&& cp /root/go/bin/mhsendmail /usr/bin/mhsendmail  
  
RUN a2enmod headers rewrite expires deflate  
  
CMD ["apache2-foreground"]  


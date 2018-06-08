FROM php:7-fpm  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libxslt1-dev \  
libicu-dev \  
git \  
npm \  
nodejs-legacy \  
&& docker-php-ext-install iconv \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install exif  
  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install xsl  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install opcache  
RUN docker-php-ext-install zip  
  
RUN curl https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN npm install -g npm && \  
npm install gulp --global  
  
RUN groupmod -g 1000 www-data  
RUN usermod -u 1000 -s /bin/bash www-data  
RUN chown -R www-data:www-data /var/www  
COPY inputrc /var/www/.inputrc  
COPY entrypoint.sh /var/www/entrypoint.sh  
  
WORKDIR /srv/app  
  
CMD ["php-fpm"]  
ENTRYPOINT ["/var/www/entrypoint.sh"]  


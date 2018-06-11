FROM php:5.6-apache  
  
WORKDIR /  
RUN curl -sS https://getcomposer.org/installer | php  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
git \  
mysql-client \  
libicu-dev \  
&& docker-php-ext-install iconv mcrypt zip pdo_mysql mbstring intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& a2enmod rewrite  
  
WORKDIR /app  
COPY composer.lock /app/composer.lock  
COPY composer.json /app/composer.json  
RUN php /composer.phar install  
RUN chmod 777
/app/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache/Serializer  
  
RUN sed -i 's%DocumentRoot /var/www/html%#DocumentRoot /var/www/html%'
/etc/apache2/apache2.conf  
  
COPY docker/opencfp.conf /etc/apache2/sites-enabled/opencfp.conf  
COPY docker/production.dist.yml /app/config/production.yml  
COPY docker/phinx.yml.dist /app/phinx.yml  
COPY docker/php.ini /usr/local/etc/php/php.ini  
  
#ENV CFP_ENV=production  
COPY . /app  
  
CMD [ "/app/docker/run.sh" ]  


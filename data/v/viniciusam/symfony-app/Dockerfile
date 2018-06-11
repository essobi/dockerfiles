FROM php:apache  
MAINTAINER Vinicius Avellar <amvinicius@gmail.com>  
  
COPY ./apache.conf /etc/apache2/sites-available/000-default.conf  
COPY ./php.ini /usr/local/etc/php/php.ini  
  
RUN apt-get update && apt-get install -y unzip git libicu-dev php5-intl \  
&& docker-php-ext-install pdo pdo_mysql intl opcache \  
&& a2enmod rewrite \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php --install-dir=/usr/local/bin/ --filename=composer \  
&& rm composer-setup.php  
  
ENV SYMFONY_ENV prod  
ENV DATABASE_HOST 127.0.0.1  
ENV DATABASE_PORT 3306  
ENV DATABASE_NAME symfony  
ENV DATABASE_USER symfony  
  
VOLUME /var/www/html  
WORKDIR /var/www/html  
  
COPY ./startup.sh /startup.sh  
RUN chmod +x /startup.sh  
CMD ["/startup.sh"]  


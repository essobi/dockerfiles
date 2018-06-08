FROM php:5.6.35-apache  
  
ARG TIMEZONE=Europe/Amsterdam  
ENV TZ $TIMEZONE  
ENV APACHE_DOCUMENT_ROOT /opt/app/public  
  
RUN a2enmod rewrite  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  
RUN sed -i ':a;N;$!ba;s/AllowOverride None/AllowOverride All/3'
/etc/apache2/apache2.conf  
RUN apt-get update && apt-get upgrade -y  
  
# mongo  
RUN apt-get install -y libsasl2-dev\  
libssl-dev\  
git\  
zip\  
unzip  
  
RUN docker-php-ext-install pcntl  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install bcmath  
  
RUN pecl install mongodb &&\  
echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongo.ini &&\  
echo "date.timezone=$TIMEZONE" > /usr/local/etc/php/conf.d/timezone.ini  
  
RUN echo "log_errors = On\nerror_log = /dev/stderr" >
/usr/local/etc/php/conf.d/error_log.ini  
  
# composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&&\  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" &&\  
php composer-setup.php &&\  
php -r "unlink('composer-setup.php');" &&\  
mv composer.phar /usr/local/bin/composer  
  
WORKDIR /opt/app  
  
COPY . /opt/app  
  
RUN composer install  
  
EXPOSE 80  


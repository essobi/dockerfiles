FROM php:fpm  
  
COPY composer.lock composer.json /var/www/  
  
COPY database /var/www/database  
  
WORKDIR /var/www  
  
RUN apt-get update && apt-get install -y libmcrypt-dev \  
mysql-client libmagickwand-dev --no-install-recommends \  
git zip unzip htop ack-grep\  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& docker-php-ext-install mcrypt pdo_mysql  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& php composer.phar install --no-dev --no-scripts \  
&& rm composer.phar  
  
COPY . /var/www  
  
RUN chown -R www-data:www-data \  
/var/www/storage \  
/var/www/bootstrap/cache  
  
RUN php artisan optimize


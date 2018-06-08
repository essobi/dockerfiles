FROM ynokas/alpine-php7fpm:latest  
  
COPY . /var/www2  
COPY .env.stage /var/www2/.env  
  
RUN apk update  
  
WORKDIR /var/www2  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/bin \  
&& php -r "unlink('composer-setup.php');" \  
&& /bin/composer.phar global require hirak/prestissimo \  
&& php /bin/composer.phar install \  
&& /bin/composer.phar global remove hirak/prestissimo \  
&& rm /bin/composer.phar  
  
RUN chown -R www-data:www-data \  
/var/www2/storage


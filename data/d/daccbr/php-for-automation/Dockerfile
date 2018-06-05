FROM yavin/alpine-php-fpm:7.0  
RUN apk --update add php7-xdebug && rm -rf /var/cache/apk/*  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer  


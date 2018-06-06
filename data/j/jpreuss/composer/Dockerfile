FROM jpreuss/php:noxdebug  
  
ENV COMPOSER_VERSION 1.4.1  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --filename=composer --install-dir=/bin
--version=$COMPOSER_VERSION \  
&& php -r "unlink('composer-setup.php');" \  
&& composer --version  
  
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*  
  
CMD composer


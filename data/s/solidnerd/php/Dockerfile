FROM php:apache  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev libpng12-dev libfreetype6-dev libjpeg62-turbo-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-gd-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mysql  
CMD ["apache2-foreground"]  


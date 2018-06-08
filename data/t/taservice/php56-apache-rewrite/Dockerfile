FROM php:5.6-apache  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y apt-utils libfreetype6-dev libjpeg62-turbo-dev
libpng12-dev libjpeg-dev libmcrypt-dev libreadline-dev\  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install pdo_mysql mysql gd mcrypt mbstring mysqli zip  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
RUN a2enmod rewrite  
  
ENV TZ=America/Toronto  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
# Commands when creating a new container  
# CMD ["service apache2 restart"]  


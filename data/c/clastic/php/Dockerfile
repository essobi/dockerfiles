FROM php:5.6-fpm  
  
MAINTAINER Dries De Peuter <dries@nousefreak.be>  
  
RUN echo "date.timezone = Europe/Brussels" >>
/usr/local/etc/php/conf.d/timezone.ini  
  
RUN apt-get update \  
&& apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libcurl4-openssl-dev \  
libxslt-dev \  
libssl-dev \  
&& docker-php-ext-install phar curl opcache iconv mcrypt pdo_mysql mbstring
dom gd \  
&& pecl install apcu-beta \  
&& echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini \  
&& pecl install igbinary \  
&& echo extension=igbinary.so > /usr/local/etc/php/conf.d/igbinary.ini \  
&& pear channel-discover pear.twig-project.org \  
&& pear install twig/CTwig \  
&& echo extension=twig.so > /usr/local/etc/php/conf.d/twig.ini \  
&& apt-get clean  


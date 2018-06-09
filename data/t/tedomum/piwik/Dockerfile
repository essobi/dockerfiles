FROM php:apache  
  
WORKDIR /var/www/html  
  
RUN apt-get update && apt-get install -y libpng-dev libjpeg62-turbo-dev
libfreetype6-dev libmcrypt-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install mysqli mbstring gd  
  
COPY config/php.ini /usr/local/etc/php/  
  
ENV PIWIK_VERSION 3.4.0  
RUN rm -rf /var/www/html/*  
RUN curl -L -O https://builds.matomo.org/piwik-${PIWIK_VERSION}.tar.gz \  
&& tar --strip 1 -xzf piwik-${PIWIK_VERSION}.tar.gz \  
&& rm piwik-${PIWIK_VERSION}.tar.gz  
  
RUN chmod a+w /var/www/html/config  
RUN chmod a+w /var/www/html/tmp  
  
VOLUME /var/www/html/config  


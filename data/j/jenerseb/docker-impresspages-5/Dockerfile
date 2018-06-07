FROM php:5.6-apache  
MAINTAINER lexaficus  
  
RUN apt-get update && apt-get install -y rsync && rm -r /var/lib/apt/lists/*  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libicu-dev unzip g++ &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install pdo pdo_mysql  
RUN docker-php-ext-install intl  
  
VOLUME /var/www/html  
  
ENV IMPRESSPAGES_VERSION 5_0_3  
  
RUN curl -o ImpressPages.zip -SL
http://download.impresspages.org/ImpressPages_${IMPRESSPAGES_VERSION}.zip \  
&& unzip -q ImpressPages.zip -d /usr/src/ \  
&& rm ImpressPages.zip  
RUN apt-get install libicu52  
RUN apt-get purge --auto-remove -y libpng12-dev libicu-dev unzip g++  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2", "-DFOREGROUND"]


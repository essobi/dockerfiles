FROM php:5.6-apache  
MAINTAINER snappy.kop@gmail.com (http://snappytux.com)  
  
ENV BUILD_PACKAGES libmcrypt-dev libfreetype6-dev libgd-dev libcurl4-gnutls-
dev php5-dev  
RUN apt-get update \  
&& apt-get install -y $BUILD_PACKAGES \--no-install-recommends \  
&& docker-php-ext-install \  
mcrypt \  
mbstring \  
curl \  
gd \  
pdo \  
pdo_mysql \  
json \  
tokenizer \  
zip \  
&& apt-get install -y php5-cli php5-curl php-pear php5-mongo nodejs npm --no-
install-recommends \  
&& pecl install mongo  
  
# Clear packet  
RUN apt-get -y autoremove && apt-get remove --purge -y $BUILD_PACKAGES && rm
-r /var/lib/apt/lists/*  
  
# Enable mod_rewrite  
RUN a2enmod rewrite  
  
# Enalbe mongoDB  
WORKDIR /usr/local/etc/php/conf.d  
RUN touch mongo.ini && echo 'extension=mongo.so' > mongo.ini  
  
# Increase php upload file  
COPY myphp.ini ./  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Remove old default.conf & ssl-default.conf  
WORKDIR /etc/apache2/sites-available  
RUN rm ./*  
  
# Add new files  
COPY default.conf ./  
COPY default-ssl.conf ./  
RUN a2ensite default.conf  
  
WORKDIR /var/www/html  
EXPOSE 80  
EXPOSE 443  
CMD ["apache2-foreground"]  


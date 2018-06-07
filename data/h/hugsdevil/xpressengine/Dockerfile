FROM php:5.6-apache  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev wget unzip
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mysqli  
  
VOLUME /var/www/html  
  
RUN curl -o xe.zip -SL
http://download.xpressengine.com/download/18325662/22755093 \  
&& unzip -d /var/www/ xe.zip \  
&& rm -rf xe.zip  
RUN sed -i "s/\/var\/www\/html/\/var\/www\/xe/g" /etc/apache2/apache2.conf  
  
RUN mkdir -p /var/www/xe/files && chmod 707 /var/www/xe/files  
  
CMD ["apache2-foreground"]  


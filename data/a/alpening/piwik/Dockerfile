FROM php:5.6-apache  
MAINTAINER Maximilian Sedlmaier <info@fam-sedlmaier.de>  
  
RUN apt-get update && apt-get install -y \  
libjpeg62-turbo-dev \  
libpng-dev \  
libfreetype6-dev \  
libgeoip-dev \  
&& rm -r /var/lib/apt/lists/*  
  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-freetype-dir=/usr
--with-freetype2-dir=/usr \  
&& docker-php-ext-install gd pdo pdo_mysql mysqli mbstring json  
  
ENV PIWIK_VERSION 3.0.2  
RUN curl https://builds.piwik.org/piwik-$PIWIK_VERSION.tar.gz | tar xz
--strip-components=1 \  
&& chown -R www-data:www-data /var/www/html \  
&& echo "always_populate_raw_post_data=-1" | tee -a
/usr/local/etc/php/conf.d/security.ini  
  
EXPOSE 80  
CMD ["apache2-foreground"]


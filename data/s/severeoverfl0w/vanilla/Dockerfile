FROM php:5.5.30-apache  
  
ENV VANILLA_VERSION 2.2  
  
RUN docker-php-ext-install pdo pdo_mysql \  
&& apt-get update && apt-get install -y unzip \  
&& curl -sSL
"https://github.com/vanilla/vanilla/archive/release/${VANILLA_VERSION}.zip" -o
vanilla.zip \  
&& unzip vanilla.zip \  
&& cp -rT vanilla-release-${VANILLA_VERSION} /var/www/html \  
&& rm -rf vanilla* \  
&& chmod -R 777 /var/www/html/conf \  
&& chmod -R 777 /var/www/html/cache \  
&& apt-get purge -y unzip  
  
VOLUME /var/www/html/uploads  


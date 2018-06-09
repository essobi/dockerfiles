FROM php:7.1.2-apache  
MAINTAINER Michael Zender <michael@crazymonkeys.de>  
  
RUN apt-get update && apt-get install -y \  
libicu-dev \  
zlib1g-dev \  
git \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install \  
intl \  
mbstring \  
pdo_mysql \  
zip  
  
COPY install-composer /root  
RUN /root/install-composer && rm /root/install-composer  
  
RUN a2enmod rewrite  
  
CMD ["apache2-foreground"]  


FROM php:5.6-apache  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
git \  
wget \  
&& docker-php-ext-install -j$(nproc) gd mcrypt  
  
RUN wget https://codeload.github.com/star7th/showdoc/tar.gz/v1.4.3 -O
showdoc.tar.gz  
  
RUN tar -zxvf showdoc.tar.gz -C /var/www/html  
  
RUN rm ./showdoc.tar.gz  
  
RUN chmod -R 777 /var/www/html  
  
CMD ["apache2-foreground"]  


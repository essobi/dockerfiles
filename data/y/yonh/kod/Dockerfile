FROM debian:jessie  
#FROM php:5.4-apache  
ADD sources.list /etc/apt/sources.list  
# Install modules  
RUN apt-get update && apt-get install -y php5 php5-gd  
RUN sed -i "1i DirectoryIndex index.php index.html" /etc/apache2/apache2.conf  
#RUN apt-get update && apt-get install -y \  
# libfreetype6-dev \  
# libjpeg62-turbo-dev \  
# libmcrypt-dev \  
# libpng12-dev \  
# && docker-php-ext-install iconv mcrypt \  
# && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-
jpeg-dir=/usr/include/ \  
# && docker-php-ext-install gd mbstring  
EXPOSE 80  
Add kod /var/www/html  
RUN userdel www-data && useradd www-data  
RUN chown www-data /var/www/html -R  
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]  


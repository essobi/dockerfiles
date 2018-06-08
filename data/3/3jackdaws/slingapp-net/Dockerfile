FROM php:7.0-apache  
MAINTAINER Ian Murphy <ian@isogen.net>  
  
#  
RUN apt-get update  
  
RUN apt-get install -y screen  
  
RUN apt-get install -y zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install zip  
  
RUN docker-php-ext-install pdo pdo_mysql  
RUN docker-php-ext-install sockets  
  
RUN mkdir /var/www/sling; \  
mkdir /var/www/ssl/; \  
rm -f /etc/apache2/sites-enabled/*;  
  
COPY . /var/www/sling  
  
COPY docker/sling.conf /etc/apache2/sites-enabled/  
  
COPY docker/server.* /var/www/ssl/  
  
COPY docker/php.ini /usr/local/etc/php/  
  
RUN a2enmod rewrite; a2enmod ssl; a2enmod proxy_wstunnel;  
  
VOLUME /var/www/sling/  
  
WORKDIR /var/www/sling  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8001  
ENTRYPOINT bash -c "php manage.php restart;php manage.php websocket start;
bash"


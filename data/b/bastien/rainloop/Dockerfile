FROM php:7-apache  
  
RUN apt-get update && \  
apt-get install -y unzip && \  
curl -O http://repository.rainloop.net/v2/webmail/rainloop-community-
latest.zip && \  
unzip rainloop-community-latest.zip && \  
rm rainloop-community-latest.zip && \  
find . -type f -exec chmod 644 {} \; && \  
find . -type d -exec chmod 755 {} \; && \  
chown -R www-data:www-data /var/www/html && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
docker-php-ext-install pdo pdo_mysql  
  
COPY php.ini /usr/local/etc/php/conf.d/php.ini  
  
VOLUME /var/www/html/data  
EXPOSE 80  


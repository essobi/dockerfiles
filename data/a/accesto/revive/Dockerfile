FROM php:7.0-apache  
RUN docker-php-ext-install pdo mysqli pdo_mysql opcache bcmath  
RUN apt-get update && apt-get -yq install unzip && \  
rm -rf /var/lib/apt/lists/*  
RUN mkdir /tmp/revive/  
ADD https://download.revive-adserver.com/revive-adserver-4.0.0.zip
/tmp/revive/  
RUN cd /tmp/revive/ && \  
unzip revive-adserver-*.zip && \  
mv ./revive-adserver-*/* /var/www/html/ && \  
rm -f /var/www/html/index.html && \  
chown -R www-data:www-data /var/www/html && \  
rm -rf /tmp/revive  
  
  
  


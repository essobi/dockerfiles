FROM php:7.1.3-apache  
  
RUN apt-get update && \  
apt-get install unzip && \  
apt-get clean && \  
curl -L -O https://github.com/Studio-42/elFinder/archive/2.1.23.zip && \  
unzip *.zip && \  
rm -f *.zip && \  
mv elFinder-* elFinder && \  
chown -R www-data:www-data elFinder && \  
mv elFinder/php/connector.minimal.php-dist elFinder/php/connector.minimal.php
&& \  
rm -rf elFinder/files && \  
ln -s /data /var/www/html/elFinder/files  
  
VOLUME /data


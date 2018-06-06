FROM shinymayhem/apache  
  
#install php extensions  
RUN a2enmod rewrite  
  
#copy apache and site config  
COPY config/php.ini /usr/local/etc/php/  
COPY config/nodify-site.conf /etc/apache2/sites-available/000-default.conf  
COPY config/apache2.conf /etc/apache2/apache2.conf  
  
COPY src/ /var/www/html  
RUN \  
apt-get update && \  
apt-get install -y git php5-curl && \  
rm -rf /var/lib/apt/lists/* && \  
cd /var/www/html && \  
php composer.phar install  
  
ENV INDEX_DIR /var/www/html/public  
ENV APPLICATION_ENV production  
#php.ini settings  
ENV DISPLAY_ERRORS Off  
ENV ERROR_REPORTING E_NONE  


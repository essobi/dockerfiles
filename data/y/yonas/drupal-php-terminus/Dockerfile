FROM wodby/drupal-php:7.0  
MAINTAINER Yonas Yanfa <yonas@savaslabs.com>  
  
# Install Terminus  
RUN cd /tmp && \  
wget https://github.com/pantheon-systems/terminus/archive/0.13.x.zip && \  
unzip 0.13.x.zip && \  
cd ./terminus-0.13.x && \  
composer install && \  
ln -s /tmp/terminus-0.13.x/bin/terminus /usr/local/bin/terminus && \  
chmod 755 /usr/local/bin/terminus  
  
COPY drupal-php-setup.sh /tmp/  
COPY terminus-setup.sh /tmp/  
COPY search-api-setup.sh /tmp/  
COPY settings.local.php /tmp/  
  
WORKDIR /var/www/html  
VOLUME /var/www/html  
EXPOSE 9000  
USER root  
  
CMD /tmp/drupal-php-setup.sh  


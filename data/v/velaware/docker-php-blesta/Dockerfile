FROM php:5.6-apache  
  
# Package installs  
RUN apt-get update && apt-get install -y unzip php5-gmp php5-mcrypt libxml2
libcurl4-openssl-dev libgmp-dev libgd-dev libc-client-dev libkrb5-dev
libmcrypt-dev && rm -r /var/lib/apt/lists/*  
  
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h  
  
# PECL installs  
RUN pecl install mailparse-2.1.6  
  
# Enabling any extensions like from above (along with other Dockerizing of PHP
stuff)  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl  
RUN docker-php-ext-enable mailparse  
RUN docker-php-ext-install pdo pdo_mysql curl imap gmp mbstring mcrypt gd  
  
RUN apt-get clean  
  
# Download the version of Blesta and unzip it, then remove the zip file  
RUN cd /tmp \  
&& curl -s -O
https://account.blesta.com/client/plugin/download_manager/client_main/download/91/blesta-4.0.0.zip
\  
&& unzip -qq blesta-4.0.0.zip \  
&& rm blesta-4.0.0.zip \  
&& mv uploads /var/www \  
&& mv blesta/* blesta/.h* /var/www/html  
  
RUN chown -R www-data: /var/www/html  
  
# ionCube support  
RUN cd /tmp \  
&& curl -s -o ioncube.tar.gz
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -zxf ioncube.tar.gz \  
&& mv ioncube/ioncube_loader_lin_5.6.so /usr/local/lib/php/extensions/* \  
&& rm -Rf ioncube.tar.gz ioncube \  
&& echo "zend_extension=ioncube_loader_lin_5.6.so" >
/usr/local/etc/php/conf.d/00_docker-php-ext-ioncube.ini  
  
RUN rm -rf /tmp/*  
  
EXPOSE 80  
# Apache mods to enable  
RUN a2enmod rewrite  
  
ENTRYPOINT ["apache2-foreground"]  


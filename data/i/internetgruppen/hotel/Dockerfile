FROM php:5.6-apache  
  
# Install basic extensions  
RUN apt-get update && apt-get install -y libpng-dev libpq-dev iputils-ping
dnsutils less && apt-get -y purge exim4 && apt-get -y autoremove && apt-get
clean  
RUN docker-php-ext-install opcache gd pdo_mysql mysql && apt-get purge gcc -y
&& rm -fr /usr/lib/gcc/  
  
# Enable/disable apache modules  
RUN a2enmod rewrite && a2dismod -f deflate  
  
RUN rm -fr /var/lock && rm -fr /var/run  


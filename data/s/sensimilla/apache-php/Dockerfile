FROM php:5.6-apache  
  
RUN a2enmod rewrite ssl headers authnz_ldap  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libldap2-dev
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap --with-ldap=/usr \  
&& docker-php-ext-install ldap \  
&& docker-php-ext-install mysqli  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/apache2/access.log  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
  
CMD ["apache2-foreground"]


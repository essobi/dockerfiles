FROM php:5.6-apache  
  
MAINTAINER Thiago Ramos Fanfoni < thiagofanfoni@gmail.com >  
  
# Upgrade aware volumes.  
VOLUME [ \  
"/var/www/html/backups" ,\  
"/var/www/html/files" ,\  
"/var/www/html/includes" ,\  
"/var/www/html/upload" ,\  
"/var/salt" \  
]  
  
# Install dependencies for PHP.  
RUN apt-get update \  
&& apt-get -y install --no-install-recommends \  
libldap2-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& ln -sf /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /usr/share/man/*  
  
# Install and configure PHP dependencies for TeamPass.  
RUN docker-php-ext-install -j$(nproc) \  
bcmath \  
gd \  
ldap \  
mbstring \  
mcrypt \  
mysqli \  
&& echo 'max_execution_time = 60' > /usr/local/etc/php/conf.d/docker-php-
custom.ini \  
&& rm -rf /usr/src/*  
  
# TeamPass Version (leave it down here for better use of the build cache).  
ENV VERSION 2.1.25.0  
# Extract the application from entrypoint to use volumes.  
COPY entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["entrypoint.sh"]  
  
# Run the Apache.  
CMD ["apache2-foreground"]  


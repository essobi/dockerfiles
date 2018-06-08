FROM owncloud:8.2-fpm  
# Install modules  
RUN apt-get update && apt-get install -y \  
libldap2-dev \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap  
CMD ["php-fpm"]  


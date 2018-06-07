FROM wordpress  
  
#Found here: https://github.com/docker-
library/php/issues/75#issuecomment-82075678  
# Install needed php extensions: ldap  
RUN \  
apt-get update && \  
apt-get install libldap2-dev -y && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  
  


# An ownCloud container with LDAP libs, a redis server, all with php-fpm  
# Start from ownCloud with php-fpm  
FROM owncloud:8-fpm  
MAINTAINER Sebastien Collin <sebastien.collin@sebcworks.fr>  
  
# Install ldap libs, redis server and supervisor  
RUN apt-get update && \  
apt-get install -y libldap2-dev \  
redis-server \  
supervisor  
  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install ldap  
  
# Prepare for redis server  
RUN mkdir /tmp/redis && \  
chmod 750 /tmp/redis && \  
chown redis:www-data /tmp/redis  
  
# Config supervisord to start apache (or php-fpm) and redis-server  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY redis-conf /redis-conf  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["oc_start"]  


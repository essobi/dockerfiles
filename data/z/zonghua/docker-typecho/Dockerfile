FROM php:7.1.7-fpm  
  
ADD ./sources.list /tmp  
  
# using 163 souces  
RUN cat /tmp/sources.list > /etc/apt/sources.list  
  
ENV AUTH_USER=admin  
ENV AUTH_PASSWORD=adminadmin  
  
  
# install extensions and typecho  
RUN apt-get update && \  
apt-get install libcurl4-openssl-dev sqlite3 libsqlite3-dev libpq-dev -y && \  
docker-php-ext-install pdo_mysql pdo_pgsql && \  
apt-get install apache2-utils -y  
  
ADD src /var/www/src  
RUN sed -i 's/\r//g' /var/www/src/docker-entrypoint.sh  
  
VOLUME /var/www/html/  
VOLUME /var/www/src/  
  
ENTRYPOINT ["sh", "/var/www/src/docker-entrypoint.sh"]  
# ENTRYPOINT ls /var/www/src  


FROM romash/docker-nginx-php:5.6  
MAINTAINER Romash <tcp6000@gmail.com>  
  
ENV INSTALL_PATH /var/www/html  
RUN cd $INSTALL_PATH && \  
wget
https://github.com/roundcube/roundcubemail/releases/download/1.2.3/roundcubemail-1.2.3-complete.tar.gz
&& \  
tar -xzf roundcubemail-1.2.3-complete.tar.gz && \  
cd roundcubemail-1.2.3 && \  
mv composer.json-dist composer.json && \  
composer install --no-dev && \  
chown www-data:www-data -R temp && \  
chown www-data:www-data -R logs  
  
WORKDIR /var/www/html  
  
COPY rootfs /  


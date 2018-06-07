FROM php:7.0-apache  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt update && apt-get install -y wget && apt upgrade -y  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list \  
&& wget -O- https://www.dotdeb.org/dotdeb.gpg | apt-key add - \  
&& apt update \  
&& apt-get install -y php7.0-mysql \  
&& docker-php-ext-install pdo mysqli pdo_mysql  
  
RUN a2enmod rewrite  
  
# this is insecure, not used in production sites, will be overwritten by
docker-compose, e.g.  
# volumes:  
# - .:/var/www/html  
# - ./docker-apache2.conf:/etc/apache2/conf-enabled/docker-apache2.conf  
# - ./docker-htpasswd:/etc/httpd/.htpasswd  
RUN mkdir /etc/httpd && echo 'admin:$apr1$E/TAfPYn$SK9JzdKwBDBsJaJrsbw.w.' >
/etc/httpd/.htpasswd  


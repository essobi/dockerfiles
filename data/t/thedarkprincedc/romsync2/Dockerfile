FROM k0st/alpine-apache-php:latest  
MAINTAINER FAN ZHISHEN <thedarkprincedc@yahoo.com>  
  
ENV TIMEZONE="US/United States" \  
PHP_MEMORY_LIMIT="512M" \  
MAX_UPLOAD="50M" \  
PHP_MAX_FILE_UPLOAD="200" \  
PHP_MAX_POST="100M"  
  
RUN apk update \  
&& apk add php-pdo_mysql \  
&& mkdir /init-start \  
&& cd $_ \  
&& wget -O romsync.zip http://repo.thedarkprincedc.com/artifactory/generic-
local/romsync.zip \  
&& unzip romsync.zip \  
&& cp -r dist/.* /app \  
&& chmod -R +r /app/resources/* \  
&& chmod 755 /app/resources/logs/* \  
&& chown apache /app/resources/logs/*  
  
EXPOSE 80/tcp  


FROM php:7.2-fpm  
  
MAINTAINER Nicolas Thal <nico.th4l@gmail.com>  
MAINTAINER Jérémy GIGNON <jeremy@gignon.fr>  
  
COPY config/php.ini /usr/local/etc/php/  
  
RUN pecl install redis \  
&& docker-php-ext-enable redis  
  
RUN docker-php-ext-enable opcache  
  
RUN apt-get update \  
&& apt-get install -y wget gnupg2 \  
&& wget -O - https://packagecloud.io/gpg.key | apt-key add - \  
&& echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list \  
&& apt-get update \  
&& apt-get install blackfire-agent \  
&& apt-get install blackfire-php  


FROM debian:jessie  
  
MAINTAINER <info@netpositive.hu>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
wget \  
curl \  
ca-certificates  
  
RUN echo "deb http://packages.dotdeb.org jessie all\ndeb-src
http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list  
RUN wget http://www.dotdeb.org/dotdeb.gpg -O /tmp/dotdeb.gpg && apt-key add
/tmp/dotdeb.gpg && rm /tmp/dotdeb.gpg  
RUN apt-get update  
  
# PHP  
RUN apt-get install -y \  
git \  
php7.0-json \  
php7.0-curl \  
php7.0-mysql \  
php7.0-gd \  
php7.0-xml \  
php7.0-zip \  
php7.0-memcached \  
php7.0-mbstring \  
php7.0-bcmath \  
php7.0-soap \  
php-intl  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  
  


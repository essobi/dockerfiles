FROM php:7.2-apache-stretch  
  
ENV VERSION_MAJOR=1.30  
ENV VERSION_MINOR=1.30.0  
RUN docker-php-ext-install \  
mysqli \  
pdo \  
pdo_mysql  
RUN apt-get update \  
&& apt-get upgrade -y  
RUN curl
"https://releases.wikimedia.org/mediawiki/${VERSION_MAJOR}/mediawiki-${VERSION_MINOR}.tar.gz"
> /mediawiki.tar.gz \  
&& tar -xav -C /var/www -f /mediawiki.tar.gz \  
&& rm -rf /var/www/html \  
&& mv /var/www/mediawiki-* /var/www/html \  
&& chown -R root:root /var/www/html  
RUN apt-get autoremove --purge -y \  
&& rm -rf /var/lib/apt/lists/* /mediawiki.tar.gz  
  
VOLUME "/var/www/html/LocalSettings.php"  
VOLUME "/var/www/html/cache"  
VOLUME "/var/www/html/images"  


FROM php:5.6-apache  
  
RUN apt-get update && \  
apt-get install -y \  
zlib1g-dev  
  
RUN curl -fsSL
'https://xcache.lighttpd.net/pub/Releases/3.2.0/xcache-3.2.0.tar.gz' -o
xcache.tar.gz \  
&& mkdir -p /tmp/xcache \  
&& tar -xf xcache.tar.gz -C /tmp/xcache --strip-components=1 \  
&& rm xcache.tar.gz \  
&& docker-php-ext-configure /tmp/xcache --enable-xcache \  
&& docker-php-ext-install /tmp/xcache \  
&& rm -r /tmp/xcache \  
&& docker-php-ext-install pdo_mysql mysqli zip \  
&& ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load  
  
COPY . /var/www/html  
  
ENV PORT 80  
  
EXPOSE 80  


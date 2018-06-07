FROM php:7.2.6-apache-stretch  
  
RUN apt-get -qq update \  
&& apt-get install \--assume-yes \--quiet \--no-install-recommends \  
ca-certificates curl git libpng-dev libfreetype6-dev libjpeg62-turbo-dev \  
libicu-dev libxml++2.6-dev \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ > /dev/null \  
&& docker-php-ext-install bcmath exif gd intl pdo_mysql soap zip xml \  
&& docker-php-ext-enable opcache \  
&& docker-php-source delete > /dev/null \  
# remove dev-dependencies  
&& apt-get remove \--assume-yes \--quiet libpng-dev libfreetype6-dev
libjpeg62-turbo-dev libicu-dev libxml++2.6-dev \  
&& rm -r /var/lib/apt/lists/*  
  
# Configure time  
RUN rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime \  
# Install composer  
&& curl -sS https://getcomposer.org/installer | \  
php -- \--install-dir=/usr/bin/ \--filename=composer \  
# Configure apache mods  
&& ln -s /etc/apache2/mods-available/expires.load /etc/apache2/mods-enabled/ \  
&& ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled/ \  
&& ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/ \  
# Setup user/group  
&& groupadd -g 1000 appuser \  
&& useradd -r -u 1000 -g appuser appuser  
  
COPY vhost.conf /etc/apache2/sites-available/000-default.conf  
COPY php.ini /usr/local/etc/php  
RUN sed -i "s/80/8000/g" /etc/apache2/ports.conf \  
&& mkdir -p /var/run/apache2 \  
&& chown -R appuser: /var/run/apache2/ \  
&& chown -R appuser: /var/www  
EXPOSE 8000  
  
USER appuser  
WORKDIR "/var/www"  
CMD ["apache2-foreground"]  


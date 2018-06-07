FROM php:7.1.0-apache  
MAINTAINER Christian Koep <christiankoep@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
git \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone -b master --depth 1 https://github.com/domainmod/domainmod.git
/var/www/html \  
&& cd /var/www \  
&& chown -R www-data:www-data /var/www \  
&& rm -rf /var/www/html/.git \  
&& docker-php-ext-install mysqli  
  
COPY _includes/config.SAMPLE.inc.php /var/www/html/_includes/config.inc.php  
RUN sed -i s/localhost/db/g /var/www/html/_includes/config.inc.php  
RUN sed -i s'/\/dm//'g /var/www/html/_includes/config.inc.php


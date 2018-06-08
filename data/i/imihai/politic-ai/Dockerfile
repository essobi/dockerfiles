FROM phpdockerio/php72-fpm:latest  
WORKDIR "/application"  
COPY /application ./  
RUN ls  
  
RUN ls  
# Fix debconf warnings upon build  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Install selected extensions and other stuff  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php7.2-pgsql php7.2-odbc \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
COPY /phpdocker/php-fpm/php-ini-overrides.ini
/etc/php/7.2/fpm/conf.d/99-overrides.ini


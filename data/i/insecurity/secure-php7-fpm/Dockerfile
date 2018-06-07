FROM php:7.1-fpm  
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>  
# https://www.noobunbox.net/serveur/auto-hebergement/installer-php-7-1-sous-
debian-et-ubuntu  
  
# Set apt-get to automatically retry if a package download fails and  
# Set apt-get --no-install-recommend/--no-install-suggest values  
RUN echo 'Acquire::Retries "5";' > /etc/apt/apt.conf.d/99AcquireRetries \  
&& echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
  
# Upgrade image \  
  
&& dpkg-divert --local --rename /usr/bin/ischroot && ln -sf /bin/true
/usr/bin/ischroot \  
&& apt-get update \  
&& LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y wget ca-
certificates vim-tiny curl unzip apt-transport-https lsb-release \  
&& apt-get dist-upgrade --no-install-recommends -y \  
  
# Security - Fix UID/GID of nginx user \  
&& usermod -u 3005 www-data \  
&& groupmod -g 3005 www-data \  
  
# Install libs for GD \  
&& wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& apt-get update && apt-get install -y --no-install-recommends \  
libbz2-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
  
# Compile, Intsall and Enable mysqli and gd \  
&& docker-php-ext-install mysqli gd \  
&& docker-php-ext-enable mysqli gd \  
  
# Clean-UP \  
&& apt-get remove -y software-properties-common \  
&& apt-get clean \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  


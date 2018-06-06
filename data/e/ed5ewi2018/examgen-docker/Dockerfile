FROM phpdockerio/php72-fpm:latest  
WORKDIR "/application"  
# Fix debconf warnings upon build  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Install selected extensions and other stuff  
RUN apt-get update \  
&& apt-get -y install php7.2-mysql php-xdebug php-pear libmcrypt-dev
libreadline-dev php7.2-dev git texlive-full \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
RUN pear config-set php_ini /etc/php/7.2/fpm/php.ini \  
&& pecl config-set php_ini /etc/php/7.2/fpm/php.ini \  
&& pecl install mcrypt-1.0.1 \  
&& echo extension=/usr/lib/php/20170718/mcrypt.so >
/etc/php/7.2/cli/conf.d/mcrypt.ini \  
&& echo extension=/usr/lib/php/20170718/mcrypt.so >
/etc/php/7.2/fpm/conf.d/mcrypt.ini  
  
  


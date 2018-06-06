# Would you like to use another custom folder than $ZSH/custom?  
FROM php:7.0.9-fpm-alpine  
MAINTAINER ChasonTang <chasontang@gmail.com>  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \--install-dir=/usr/local/bin \--filename=composer \  
&& php -r "unlink('composer-setup.php');"


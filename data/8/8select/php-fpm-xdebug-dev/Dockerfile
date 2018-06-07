FROM 8select/php-fpm-xdebug:0.4.1  
  
MAINTAINER Andreas Kleiber <andreas.kleiber@8select.de>  
  
RUN php -r "readfile('https://getcomposer.org/installer');" | php --
\--install-dir=/usr/local/bin \--filename=composer  
RUN apt-get update  
RUN apt-get install -y git zip unzip  
RUN apt-get clean  


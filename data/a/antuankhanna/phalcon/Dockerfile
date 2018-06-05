FROM php:5.6-apache  
MAINTAINER Antuan Khanna <antuan@antuankhanna.com>  
  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV PHALCON_TAG phalcon-v2.0.13  
WORKDIR /phalcon  
ADD https://github.com/phalcon/cphalcon/archive/$PHALCON_TAG.tar.gz
./phalcon.tar.gz  
  
COPY apache.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN a2enmod rewrite\  
&& apt-get update\  
&& apt-get -y install php5-dev libpcre3-dev gcc make php5-mysql\  
&& apt-get autoremove\  
&& apt-get clean\  
&& tar -xzf phalcon.tar.gz\  
&& cd cphalcon-$PHALCON_TAG/build\  
&& ./install\  
&& rm -rf /phalcon\  
&& echo 'extension=phalcon.so' | tee /usr/local/etc/php/conf.d/30-phalcon.ini\  
&& echo '<?php phpinfo();' | tee /var/www/html/index.php  


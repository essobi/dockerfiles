FROM kibatic/symfony:5.6  
MAINTAINER Kitpages <system@kibatic.com>  
  
RUN apt-get -qqq update && DEBIAN_FRONTEND=noninteractive apt-get install -qqq
-y \  
php5-gd \  
php5-mysql \  
php5-xmlrpc \  
php-soap \  
php5-curl \  
php5-mcrypt \  
php5-json \  
php5-mongo \  
php5-apcu \  
imagemagick \  
libpng12-0 \  
libpng12-dev \  
libjpeg62-turbo \  
libjpeg62-turbo-dev \  
wkhtmltopdf \  
xvfb \  
pdftk && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD config/supervisor/conf.d/app-log.conf /etc/supervisor/conf.d/app-log.conf  
  
RUN chgrp www-data -R /tmp && chmod g+rwx -R /tmp  


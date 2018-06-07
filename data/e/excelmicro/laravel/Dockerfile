FROM excelmicro/php:v5.5.9  
MAINTAINER Ani Channarasappa <achannarasappa@excelmicro.com>  
  
WORKDIR /app  
RUN apt-get update && \  
apt-get -y install \  
git-core \  
php5-mcrypt  
RUN php5enmod mcrypt  
RUN mkdir app && \  
mkdir app/storage && \  
mkdir app/storage/meta && \  
mkdir app/storage/logs && \  
mkdir app/storage/sessions && \  
chgrp -R www-data app/storage  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
ADD apache_laravel /etc/apache2/sites-available/000-default.conf  
ONBUILD ADD . /app  
ONBUILD RUN composer install  
ONBUILD RUN chmod 777 -R /app/app/storage  


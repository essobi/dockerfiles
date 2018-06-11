FROM zulumarketing/app-server  
MAINTAINER Carlos Killpack <carlos@zulumarketing.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update > /dev/null \  
&& apt-get upgrade -y > /dev/null \  
&& apt-get -y install php5-fpm php5-mysql php5-gd php5-intl php5-imagick
php5-mcrypt \  
php5-curl php5-cli php5-xdebug > /dev/null  
  
COPY supervisor.conf /etc/supervisor/conf.d/php5-fpm.conf  
COPY php-fpm.conf /etc/php5/fpm/php-fpm.conf  
COPY php.ini /etc/php5/fpm/php.ini  
  
EXPOSE 80  


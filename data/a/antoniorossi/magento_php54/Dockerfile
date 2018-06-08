FROM antoniorossi/magento_apache  
MAINTAINER antoniorossi <antoniorossi@outlook.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y install php5 php5-curl php5-gd php5-mcrypt
php5-mysql && apt-get clean  
  
COPY php.ini /etc/php5/apache2/  
COPY info.php /var/www/magento/  


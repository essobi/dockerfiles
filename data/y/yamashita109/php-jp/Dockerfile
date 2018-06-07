FROM yamashita109/web-jp:centos72trad-apache2  
  
MAINTAINER yamashita109  
  
RUN yum -y update \  
&& yum -y install \  
php \  
php-cli \  
php-gd \  
php-intl \  
php-mbstring \  
php-mysqlnd \  
php-pdo \  
php-xml \  
php-mcrypt \  
composer \  
&& yum clean all \  
&& rm -rf /var/cache/yum/*;  


FROM widgento/magento  
MAINTAINER Widgento  
  
ADD /etc/php5/fpm/conf.d/21-customdebug.ini
/etc/php5/fpm/conf.d/21-customdebug.ini  
ADD /etc/nginx/fastcgi_params_magento.conf
/etc/nginx/fastcgi_params_magento.conf  
ADD /init.sh /tmp/init.sh  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y \  
php5-xdebug \  
&& chmod +x /tmp/init.sh  
  


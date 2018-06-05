FROM php:5.6.32-fpm-alpine  
MAINTAINER billypon  
  
ADD *.ini /etc/php5/conf.d/  
ADD *.so /usr/lib/php5/modules/  
  
RUN apk add --no-cache php5-bcmath php5-bz2 php5-calendar php5-exif php5-gd
php5-gettext php5-gmp php5-imagick php5-mcrypt php5-mysql php5-mysqli
php5-pcntl php5-pdo_mysql php5-soap php5-sockets php5-xmlrpc php5-xsl && \  
for x in `echo dom pdo xml`; do rm -f /etc/php5/conf.d/$x.ini; rm -f
/usr/lib/php5/modules/$x.so; done && \  
for x in `ls /etc/php5/conf.d`; do ln -s /etc/php5/conf.d/$x
/usr/local/etc/php/conf.d; done && \  
for x in `ls /usr/lib/php5/modules`; do ln -s /usr/lib/php5/modules/$x
/usr/local/lib/php/extensions/*; done && \  
  
# zend loader  
#wget http://downloads.zend.com/guard/7.0.0/zend-loader-
php5.6-linux-x86_64_update1.tar.gz -O - | tar zx -C /tmp && \  
#cp /tmp/zend-loader-*/ZendGuardLoader.so /usr/local/lib/php/extensions/* && \  
#rm -rf /tmp/zend-loader-* && \  
  
sleep 0  


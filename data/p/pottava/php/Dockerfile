# PHP v5.6 & Apache v2.4  
#  
# docker run \--rm pottava/php:5.6 php -v  
# docker run -v `pwd`/html:/var/www/localhost/htdocs pottava/php:5.6  
# docker run -v `pwd`/httpd.conf:/etc/apache2/httpd.conf pottava/php:5.6  
  
FROM alpine:3.3  
  
RUN apk --no-cache add apache2 php-apache2 \  
php php-fpm php-json php-zlib php-xml php-pdo php-phar \  
php-openssl php-curl php-pdo_mysql php-mysql php-mysqli \  
php-gd mysql-client \  
&& mkdir -p /run/apache2/ \  
&& rm -rf /var/www/localhost/htdocs/index.html \  
&& echo -e "<?php\nphpinfo();" > /var/www/localhost/htdocs/index.php \  
&& chmod 755 -R /var/www/ \  
&& ln -sf /dev/stdout /var/log/apache2/access.log \  
&& ln -sf /dev/stderr /var/log/apache2/error.log  
  
VOLUME /var/www/localhost/htdocs  
EXPOSE 80  
  
CMD ["httpd", "-D", "FOREGROUND"]  


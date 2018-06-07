FROM alpine:3.4  
  
MAINTAINER toricls  
  
RUN echo "@community http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk --no-cache add apache2 php7-apache2@community \  
php7@community php7-gd@community php7-xml@community php7-xsl@community
php7-pdo_mysql@community \  
php7-mbstring@community php7-mcrypt@community php7-curl@community
php7-json@community php7-fpm@community \  
php7-phar@community php7-openssl@community php7-xml \  
php7-mysqlnd@community php7-ctype@community php7-zlib@community
php7-zip@community && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
mkdir -p /run/apache2  
  
WORKDIR /var/www/localhost/htdocs  
  
EXPOSE 80  
  
CMD ["httpd", "-D", "FOREGROUND"]


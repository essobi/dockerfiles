FROM alpine:3.3  
RUN addgroup -g 1000 -S www-data \  
&& adduser -u 1000 -D -S -G www-data www-data  
  
RUN apk --update add \  
supervisor \  
nginx ca-certificates \  
php-fpm php-zip php-json php-zlib php-xml php-pdo php-phar php-openssl \  
php-pdo_mysql php-mysql php-mysqli \  
php-gd php-iconv php-mcrypt \  
php-common php-curl php-pgsql php-imap php-cgi fcgi \  
php-pdo php-pdo_pgsql php-soap php-xmlrpc php-posix php-gettext php-ldap php-
ctype php-dom \  
git \  
&& \  
rm -rf /tmp/src && \  
rm -fr /var/lib/apk/* && \  
rm -rf /var/cache/apk/*  
  
ADD ./config/start.sh /home/  
  
ADD ./config/php.ini /home/defaults/  
ADD ./config/php-fpm.conf /home/defaults/  
ADD ./config/nginx.conf /home/defaults/  
ADD ./config/supervisord.conf /etc/  
  
RUN chmod u+x /home/start.sh  
  
CMD ["/home/start.sh"]  


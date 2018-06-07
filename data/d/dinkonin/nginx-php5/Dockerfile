FROM alpine:3.4  
RUN apk update && \  
apk add nginx bash ca-certificates s6 curl php php5-phar php5-curl\  
php5-fpm php5-json php5-zlib php5-xml php5-dom php5-ctype php5-opcache
php5-zip php5-iconv \  
php5-pdo php5-pdo_mysql php5-pdo_sqlite php5-pdo_pgsql php5-memcache\  
php5-gd php5-mcrypt php5-openssl php5-sockets php5-posix php5-ldap php5-pgsql
&& \  
rm -rf /var/cache/apk/* && \  
# ln -s /usr/bin/php /usr/bin/php && \  
rm -f /etc/php/php5-fpm.d/www.conf && \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/community \  
shadow  
  
RUN curl -sS https://getcomposer.org/installer | php --
--filename=/usr/local/bin/composer  
  
RUN rm -rf /var/www/* && mkdir /www/  
COPY files/php/conf.d/local.ini /etc/php5/conf.d/  
COPY files/php/php-fpm.conf /etc/php5/  
COPY files/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY files/nginx/php.conf /etc/nginx/php.conf  
COPY files/nginx/proxy.conf /etc/nginx/proxy.conf  
COPY files/services.d /etc/services.d  
  
# Fix permissions  
RUN chmod +x /etc/services.d/php/run && chmod +x /etc/services.d/nginx/run  
RUN groupmod -o -g "1000" nginx && usermod -o -u "1000" nginx  
EXPOSE 80  
ENTRYPOINT ["/bin/s6-svscan", "/etc/services.d"]  
CMD []  


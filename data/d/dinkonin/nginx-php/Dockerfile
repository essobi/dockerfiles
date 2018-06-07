FROM alpine:edge  
  
RUN apk update && \  
apk add nginx bash ca-certificates s6 curl ssmtp php7 php7-phar php7-curl\  
php7-fpm php7-json php7-zlib php7-xml php7-dom php7-ctype php7-opcache
php7-zip php7-iconv \  
php7-pdo php7-pdo_mysql php7-pdo_sqlite php7-pdo_pgsql php7-mbstring
php7-session \  
php7-gd php7-mcrypt php7-openssl php7-sockets php7-posix php7-ldap php7-pgsql
&& \  
rm -rf /var/cache/apk/* && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
rm -f /etc/php7/php-fpm.d/www.conf && \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/community \  
shadow && \  
touch /etc/php7/php-fpm.d/env.conf  
  
RUN curl -sS https://getcomposer.org/installer | php --
--filename=/usr/local/bin/composer  
  
RUN rm -rf /var/www/* && mkdir /www/  
COPY files/php/conf.d/local.ini /etc/php7/conf.d/  
COPY files/php/php-fpm.conf /etc/php7/  
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


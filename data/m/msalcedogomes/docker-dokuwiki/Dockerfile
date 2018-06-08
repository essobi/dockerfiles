FROM alpine:3.4  
MAINTAINER Ilya Stepanov <dev@ilyastepanov.com>  
  
RUN apk --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/main/ --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ add \  
php7 php7-fpm libpng php7-gd php7-session php7-openssl php7-xml nginx
supervisor curl tar unzip || \  
(apk --no-cache --repository
http://dl-1.alpinelinux.org/alpine/edge/community/ add \  
php7 php7-fpm php7-gd php7-session php7-openssl openssl php7-xml nginx
supervisor curl tar unzip) || \  
(apk --no-cache --repository
http://dl-2.alpinelinux.org/alpine/edge/community/ add \  
php7 php7-fpm php7-gd php7-session php7-openssl openssl php7-xml nginx
supervisor curl tar unzip) || \  
(apk --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/community/  add \  
php7 php7-fpm php7-gd php7-session php7-openssl openssl php7-xml nginx
supervisor curl tar unzip) || \  
(apk --no-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/community/ add \  
php7 php7-fpm php7-gd php7-session php7-openssl openssl php7-xml nginx
supervisor curl tar unzip) || \  
(apk --no-cache --repository
http://dl-5.alpinelinux.org/alpine/edge/community/ add \  
php7 php7-fpm php7-gd php7-session php7-openssl openssl php7-xml nginx
supervisor curl tar unzip) || \  
(apk --no-cache --repository
http://dl-6.alpinelinux.org/alpine/edge/community/ add \  
php7 php7-fpm php7-gd php7-session php7-openssl openssl php7-xml nginx
supervisor curl tar unzip)  
  
RUN mkdir -p /run/nginx  
  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php7/php-fpm.ini && \  
sed -i -e "s|;daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf &&
\  
sed -i -e "s|listen\s*=\s*127\\.0\\.0\\.1:9000|listen = /var/run/php-
fpm7.sock|g" /etc/php7/php-fpm.d/www.conf && \  
sed -i -e "s|;listen\\.owner\s*=\s*|listen.owner = |g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s|;listen\\.group\s*=\s*|listen.group = |g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s|;listen\\.mode\s*=\s*|listen.mode = |g" /etc/php7/php-
fpm.d/www.conf  
  
EXPOSE 80 443  
  
CMD /start.sh  


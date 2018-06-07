FROM gliderlabs/alpine:edge  
MAINTAINER Robert Bak <contact@robertbak.com>  
  
# Credit: Based on https://github.com/ulsmith/alpine-apache-php7  
# Add repo for php7  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk update && apk upgrade && apk add \  
bash apache2 php7-apache2 curl unzip \  
php7 \  
php7-mcrypt \  
php7-gd \  
php7-mbstring \  
php7-curl \  
php7-zip \  
php7-xml \  
php7-ctype \  
php7-json \  
php7-session \  
php7-openssl \  
php7-dom \  
&& cp /usr/bin/php7 /usr/bin/php \  
&& rm -f /var/cache/apk/*  
  
  
RUN mkdir /run/apache2 \  
&& sed -i "s/#LoadModule\ rewrite_module/LoadModule\ rewrite_module/"
/etc/apache2/httpd.conf \  
&& sed -i "s/#LoadModule\ session_module/LoadModule\ session_module/"
/etc/apache2/httpd.conf \  
&& sed -i "s/#LoadModule\ session_cookie_module/LoadModule\
session_cookie_module/" /etc/apache2/httpd.conf \  
&& sed -i "s/#LoadModule\ session_crypto_module/LoadModule\
session_crypto_module/" /etc/apache2/httpd.conf \  
&& sed -i "s/#LoadModule\ deflate_module/LoadModule\ deflate_module/"
/etc/apache2/httpd.conf \  
&& sed -i "s#^DocumentRoot \".*#DocumentRoot \"/app/public\"#g"
/etc/apache2/httpd.conf \  
&& sed -i "s#/var/www/localhost/htdocs#/app/public#" /etc/apache2/httpd.conf \  
&& sed -i "s/Listen 80/Listen 8080/" /etc/apache2/httpd.conf \  
&& printf "\n<Directory \"/app/public\">\n\tAllowOverride All\n</Directory>\n"
>> /etc/apache2/httpd.conf  
  
RUN mkdir /app && mkdir /app/public  
  
ENV GRAV_VERSION 1.4.5  
  
RUN curl -o /tmp/grav.zip -J -L
https://getgrav.org/download/core/grav/$GRAV_VERSION \  
&& unzip /tmp/grav.zip -d /tmp/ \  
&& rm /tmp/grav.zip \  
&& mv /tmp/grav/* /app/public/ \  
&& cp /app/public/webserver-configs/htaccess.txt /app/public/.htaccess  
  
RUN chmod -R 777 /app \  
&& touch /var/log/apache2/access.log \  
&& ln -sf /dev/stderr /var/log/apache2/error.log \  
&& chmod -R 777 /var/log/apache2/ \  
&& chmod -R 777 /run/apache2/ \  
&& chmod -R 777 /etc/  
  
ADD init.sh /app/  
  
EXPOSE 8080  
ENTRYPOINT ["app/init.sh"]  


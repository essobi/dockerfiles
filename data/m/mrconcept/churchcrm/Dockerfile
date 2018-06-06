FROM alpine:3.7  
# Add basics first  
RUN apk update && apk upgrade && apk add \  
bash apache2 php7-apache2 curl ca-certificates openssl openssh git php7
php7-phar php7-json php7-iconv php7-openssl tzdata nano  
  
# Setup apache and php  
RUN apk add \  
php7-mcrypt \  
php7-mbstring \  
php7-soap \  
php7-dom \  
php7-pdo \  
php7-zip \  
php7-mysqli \  
php7-bcmath \  
php7-gd \  
php7-pdo_mysql \  
php7-gettext \  
php7-curl \  
php7-session \  
php7-exif \  
php7-fileinfo \  
php7-xml  
  
RUN cp /usr/bin/php7 /usr/bin/php \  
&& rm -f /var/cache/apk/*  
  
# set sensible environment variables for churchcrm  
ENV PHP_UPLOAD_MAX_FILESIZE=50M  
  
# Add apache to run and configure  
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
&& sed -i "s#^DocumentRoot \".*#DocumentRoot \"/web/html\"#g"
/etc/apache2/httpd.conf \  
&& sed -i "s#/var/www/localhost/htdocs#/web/html#" /etc/apache2/httpd.conf \  
&& printf "\n<Directory \"/web/html\">\n\tAllowOverride All\n</Directory>\n"
>> /etc/apache2/httpd.conf  
  
RUN mkdir /web && mkdir /web/html && chown -R apache:apache /web && chmod -R
755 /web && mkdir bootstrap  
ADD start.sh /bootstrap/  
RUN chmod +x /bootstrap/start.sh  
  
ENTRYPOINT ["/bootstrap/start.sh"]


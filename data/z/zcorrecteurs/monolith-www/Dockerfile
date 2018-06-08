FROM alpine:3.6  
MAINTAINER Vincent <vincent@zcorrecteurs.fr>  
  
# Add basics first  
RUN apk update && \  
apk upgrade && \  
apk add \  
apache2 \  
bash \  
php7-apache2 \  
curl \  
ca-certificates \  
openssl \  
openssh \  
git \  
php7 \  
php7-phar \  
php7-json \  
php7-iconv \  
php7-openssl \  
tzdata \  
openntpd \  
nano  
  
# Add Composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# Setup apache and php  
RUN apk add --update-cache \  
php7-xdebug \  
php7-mbstring \  
php7-ldap \  
php7-dom \  
php7-pdo \  
php7-zip \  
php7-gd \  
php7-pdo_mysql \  
php7-xmlrpc \  
php7-curl \  
php7-ctype \  
php7-session \  
php7-simplexml \  
php7-xsl \  
php7-redis  
  
RUN cp /usr/bin/php7 /usr/bin/php && rm -f /var/cache/apk/*  
  
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
&& sed -i "s#^DocumentRoot \".*#DocumentRoot \"/opt/app/web\"#g"
/etc/apache2/httpd.conf \  
&& sed -i "s#/var/www/localhost/htdocs#/opt/app/web#" /etc/apache2/httpd.conf
\  
&& printf "\n<Directory \"/opt/app/web\">\n\tAllowOverride
All\n</Directory>\n" >> /etc/apache2/httpd.conf \  
&& sed -i "s/variables_order\ =\ \"GPCS\"/variables_order\ =\ \"EGPCS\"/"
/etc/php7/php.ini \  
&& sed -i "s/;date.timezone\ =/date.timezone\ =\ \"Europe\/Paris\"/"
/etc/php7/php.ini \  
&& sed -i "s/;intl.default_locale\ =/intl.default_locale\ =\ \"fr_FR.UTF-8\"/"
/etc/php7/php.ini  
  
  
# Add a custom entrypoint.  
COPY build/entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["httpd", "-D", "FOREGROUND"]  
EXPOSE 80  
  
ENV COMPOSER_CACHE_DIR=/var/cache/composer \  
SYMFONY_LOG_DIR=/var/log/symfony \  
SYMFONY_CACHE_DIR=/var/cache/symfony \  
SYMFONY_ENVIRONMENT=prod \  
SYMFONY_DEBUG=false  
  
WORKDIR /opt/app  
COPY . /opt/app


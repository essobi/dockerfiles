FROM alpine:3.5  
  
RUN set -x \  
&& apk --no-cache add \  
apache2 \  
php5 \  
php5-apache2 \  
php5-bcmath \  
php5-curl \  
php5-gettext \  
php5-intl \  
php5-json \  
php5-mcrypt \  
php5-mysqli \  
php5-opcache \  
php5-openssl \  
php5-pdo_mysql \  
php5-phar \  
php5-posix \  
php5-xdebug \  
php5-xsl \  
php5-zlib \  
&& mkdir /run/apache2 \  
&& mkdir -p /etc/apache2/vhosts.d \  
&& echo "IncludeOptional /etc/apache2/vhosts.d/*.conf" >>
/etc/apache2/httpd.conf \  
&& sed -ri \  
-e 's|^(\s*ErrorLog)\s+\S+|\1 /proc/self/fd/2|g' \  
-e '/^<IfModule log_config_module>/,/^<\/IfModule>/d' \  
-e 's/^Listen 80$/Listen 0.0.0.0:80/' \  
/etc/apache2/httpd.conf  
  
COPY conf.d/* /etc/apache2/conf.d/  
  
ENV PHP_XDEBUG_ENABLED="false" \  
PHP_XDEBUG_HOST="127.0.0.1" \  
PHP_XDEBUG_PORT="9000" \  
HTTPD_REMOTEIP_HEADER="X-Forwarded-For" \  
HTTPD_REMOTEIP_INTERNAL_PROXY="10.0.0.0/8 172.16.0.0/12 192.168.0.0/16"  
  
# Install composer  
ENV COMPOSER_VERSION 1.4.2  
ENV COMPOSER_HOME /composer  
ENV PATH /composer/vendor/bin:$PATH  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN apk add --no-cache git curl \  
&& curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r ' \  
if (hash("SHA384", file_get_contents("/tmp/composer-setup.php")) !==
trim(file_get_contents("/tmp/composer-setup.sig"))) { \  
unlink("/tmp/composer-setup.php"); echo "Invalid installer" . PHP_EOL;
exit(1); \  
}' \  
&& php /tmp/composer-setup.php --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& rm /tmp/composer-setup.*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["httpd"]  


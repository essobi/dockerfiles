FROM debian:jessie  
MAINTAINER Paul Woelfel <github@frig.at>  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
xz-utils \  
apache2-bin apache2.2-common \  
php5 php5-gd php5-intl php5-mcrypt php5-mysqlnd php5-sqlite php5-tidy \  
libapache2-mod-php5 \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
# ENV PHP_INI_DIR /etc/php  
ENV APACHE_CONFDIR /etc/apache2  
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars  
  
# Apache + PHP requires preforking Apache for best results  
RUN a2dismod mpm_event && a2enmod mpm_prefork && a2enmod rewrite  
  
# logs should go to stdout / stderr  
RUN set -ex \  
&& . "$APACHE_ENVVARS" \  
&& ln -sfT /dev/stderr "$APACHE_LOG_DIR/error.log" \  
&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/access.log" \  
&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/other_vhosts_access.log"  
  
# PHP files should be handled by PHP, and should be preferred over any other
file type  
RUN { \  
echo '<FilesMatch \\.php$>'; \  
echo '\tSetHandler application/x-httpd-php'; \  
echo '</FilesMatch>'; \  
echo; \  
echo 'DirectoryIndex disabled'; \  
echo 'DirectoryIndex index.php index.html'; \  
echo; \  
echo '<Directory /var/www/>'; \  
echo '\tOptions -Indexes'; \  
echo '\tAllowOverride All'; \  
echo '</Directory>'; \  
} | tee "$APACHE_CONFDIR/conf-available/docker-php.conf" \  
&& a2enconf docker-php  
  
COPY docker-php-entrypoint /usr/local/bin/  
  
ENTRYPOINT ["docker-php-entrypoint"]  
  
COPY apache2-foreground /usr/local/bin/  
WORKDIR /var/www/html  
  
EXPOSE 80  
CMD ["apache2-foreground"]  


FROM datenarong/docker-debian:stretch  
  
MAINTAINER Yamada Yoseigi (datenarong@gmail.com)  
  
# Install apache2  
RUN apt-get update && \  
apt-get install -y \  
apache2 \  
xz-utils  
  
# Install Library  
RUN apt-get update && \  
apt-get install -y --allow-downgrades --no-install-recommends \  
libapr1 \  
libapr1-dev \  
libaprutil1 \  
libaprutil1-dev \  
libaprutil1-ldap \  
libedit2 \  
liblua5.3-0 \  
libpcre++0v5 \  
libxml2  
  
ENV APACHE_CONFDIR /etc/apache2  
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars  
  
RUN set -ex && \  
\  
# generically convert lines like  
# export APACHE_RUN_USER=www-data  
# into  
# : ${APACHE_RUN_USER:=www-data}  
# export APACHE_RUN_USER  
# so that they can be overridden at runtime ("-e APACHE_RUN_USER=...")  
sed -ri 's/^export ([^=]+)=(.*)$/: ${\1:=\2}\nexport \1/' "$APACHE_ENVVARS" &&
\  
\  
# setup directories and permissions  
. "$APACHE_ENVVARS" && \  
for dir in \  
"$APACHE_LOCK_DIR" \  
"$APACHE_RUN_DIR" \  
"$APACHE_LOG_DIR" \  
/var/www/html \  
; do \  
rm -rvf "$dir" \  
&& mkdir -p "$dir" \  
&& chown -R "$APACHE_RUN_USER:$APACHE_RUN_GROUP" "$dir"; \  
done  
  
# Apache + PHP requires preforking Apache for best results  
RUN a2dismod mpm_event && a2enmod mpm_prefork  
  
# logs should go to stdout / stderr  
RUN set -ex && \  
. "$APACHE_ENVVARS" && \  
ln -sfT /dev/stderr "$APACHE_LOG_DIR/error.log" && \  
ln -sfT /dev/stdout "$APACHE_LOG_DIR/access.log" && \  
ln -sfT /dev/stdout "$APACHE_LOG_DIR/other_vhosts_access.log"  
  
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
} | tee "$APACHE_CONFDIR/conf-available/docker-php.conf" && \  
a2enconf docker-php  
  
ENV PHP_EXTRA_BUILD_DEPS apache2-dev  
ENV PHP_EXTRA_CONFIGURE_ARGS --with-apxs2  
  
# Remove default VirtualHost  
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf /var/www/html  
  
# Enable rewrite module  
RUN a2enmod rewrite  
  
# Configure Apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
# Clean cash  
RUN apt-get -y clean && \  
rm -r /var/lib/apt/lists/*  
  
COPY apache2-foreground /usr/local/bin/  
  
EXPOSE 80  
CMD ["apache2-foreground"]


FROM debian:jessie  
MAINTAINER portlandwebworks  
  
# Install pre-requisite software.  
RUN apt-get update \  
&& apt-get install -y php5 php5-curl php5-gd php5-mysql php5-pgsql php5-sqlite
php5-xdebug php5-xmlrpc \  
&& apt-get clean  
  
# Enable apache mods.  
RUN a2enmod rewrite \  
&& a2enmod headers  
  
# Predefine helpful, non-persistent vars.  
ARG APACHE_CONFDIR=/etc/apache2  
ARG APACHE_ENVVARS=$APACHE_CONFDIR/envvars  
ARG DOCUMENT_ROOT=/var/www/html  
ARG PHP_INI_DIR=/etc/php5/apache2/conf.d  
ARG BIN_DIR=/usr/local/bin  
  
# Rewrite envvars so that they're overridable during runtime. Then load them.  
RUN set -ex \  
&& sed -ri 's/^(#?)export ([^=]+)=(.*)$/\1: ${\2:=\3}\n\1export \2/'
"$APACHE_ENVVARS"  
  
# Make www-data owner of select apache directories.  
RUN set -ex \  
&& . "$APACHE_ENVVARS" \  
&& for dir in "$APACHE_LOCK_DIR" "$APACHE_RUN_DIR" "$APACHE_LOG_DIR"
"$DOCUMENT_ROOT"; do \  
rm -rvf "$dir" \  
&& mkdir -p "$dir" \  
&& chown -R "$APACHE_RUN_USER:$APACHE_RUN_GROUP" "$dir"; \  
done  
  
# Route logs to the standard stream.  
RUN set -ex \  
&& . "$APACHE_ENVVARS" \  
&& ln -sfT /dev/stderr "$APACHE_LOG_DIR/error.log" \  
&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/access.log" \  
&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/other_vhosts_access.log"  
  
# Copy Apache configs  
COPY drupal-apache-dev.conf "$APACHE_CONFDIR/conf-available/drupal-apache-
dev.conf"  
RUN set -ex \  
&& ln -sfT "$APACHE_CONFDIR/conf-available/drupal-apache-dev.conf"
"$APACHE_CONFDIR/conf-enabled/drupal-apache-dev.conf"  
  
# Copy PHP configs  
COPY 30-opcache.ini "$PHP_INI_DIR/"  
COPY 30-php.ini "$PHP_INI_DIR/"  
COPY 30-xdebug.ini "$PHP_INI_DIR/"  
  
# Copy entrypoint  
COPY drupal-apache-dev.sh "$BIN_DIR/drupal-apache-dev"  
  
WORKDIR /var/www/html  
EXPOSE 80  
CMD ["drupal-apache-dev"]


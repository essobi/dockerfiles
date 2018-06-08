FROM ubuntu:xenial  
MAINTAINER Pascal Martineau <pascal@lewebsimple.ca>  
  
# Install package dependencies  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >
/etc/apt/sources.list.d/ondrej-php-xenial.list \  
&& echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >>
/etc/apt/sources.list.d/ondrej-php-xenial.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C \  
&& apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
apache2 \  
ca-certificates \  
curl \  
git \  
less \  
imagemagick \  
iputils-ping \  
nano \  
openssh-client \  
php \  
php-cli \  
php-curl \  
php-gd \  
php-intl \  
php-mbstring \  
php-mcrypt \  
php7.1-mysqli \  
php-xml \  
php-zip \  
php-pear \  
php-xdebug \  
rsync \  
ssmtp \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure environment variables  
ENV APACHE_CONFDIR /etc/apache2  
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars  
ENV APACHE_UID 1000  
ENV COMPOSER_HOME /var/www/.composer  
  
# Copy configuration files  
COPY conf/ /  
  
# Configure server  
RUN set -ex \  
# Load Apache environment variables  
&& . "$APACHE_ENVVARS" \  
# Configure server FQDN  
&& a2enconf fqdn \  
# Output error log to stderr  
&& ln -sfT /dev/stderr "$APACHE_LOG_DIR/error.log" \  
&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/access.log" \  
# Enable Apache modules  
&& a2enmod expires headers proxy proxy_http rewrite ssl \  
&& apache2ctl graceful \  
# Install composer  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
  
# Install WP-CLI  
&& curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp \  
# Create XDebug directory  
&& mkdir -p /tmp/xdebug \  
# Set www-data UID and adjust permissions  
&& usermod --non-unique --uid ${APACHE_UID} www-data \  
&& groupmod --non-unique --gid ${APACHE_UID} www-data \  
&& chown -R www-data:www-data /var/www /tmp/xdebug  
  
VOLUME ["etc/apache2/sites-available","/var/www/html","/tmp/xdebug"]  
WORKDIR /var/www/html  
  
EXPOSE 80  
  
CMD ["/docker-entrypoint.sh"]  


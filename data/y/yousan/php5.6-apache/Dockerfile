FROM php:5.6-apache  
  
# @link https://github.com/docker-library/wordpress  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev
libcurl4-openssl-dev && rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache  
  
# @link https://github.com/docker-
library/php/issues/331#issuecomment-261016528 Really thanks  
RUN docker-php-ext-install curl mysqli opcache pdo pdo_mysql zip  
  
# @link https://hub.docker.com/r/plab/docker-php/~/dockerfile/  
RUN apt-get update && apt-get install -y \  
bzip2 \  
libbz2-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libghc-postgresql-libpq-dev \  
&& docker-php-ext-install mcrypt mbstring bz2 zip \  
&& docker-php-ext-configure gd -with-freetype-dir=/usr/include/ -with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/include/postgresql/ \  
&& docker-php-ext-install gd pgsql pdo_pgsql  
  
# @link https://github.com/docker-library/php/issues/57  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev libicu-dev g++ \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl  
  
# @link https://github.com/docker-library/php/issues/77#issuecomment-88936146  
RUN pecl install -o -f xdebug && \  
echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20131226/xdebug.so" > /usr/local/etc/php/conf.d/pecl-xdebug.ini  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN a2enmod rewrite expires vhost_alias  
  
# Install 'emacs' and 'less' for development  
## I MUST remove those lines when deplyoing at the future  
ADD sources.list /etc/apt/  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5
&& \  
apt-get update  
# for CakePHP  
RUN apt-get install -y emacs-nox less composer  
RUN apt-get install -y mysql-client postgresql-client php-intl php-mbstring
php-xml php-zip  
  
ENV TERM=xterm  
  
  
COPY 000-default.conf /etc/apache2/sites-available/  
RUN sed -i 's/ AllowOverride None/ AllowOverride All/'
/etc/apache2/apache2.conf  
  
VOLUME /var/www/html  
  
# Install phpMyAdmin from here  
# Include keyring to verify download  
COPY phpmyadmin.keyring /tmp/  
ENV VERSION 4.7.4  
ENV URL
https://files.phpmyadmin.net/phpMyAdmin/${VERSION}/phpMyAdmin-${VERSION}-all-
languages.tar.gz  
  
# Download tarball, verify it using gpg and extract  
RUN set -x \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& curl --output phpMyAdmin.tar.gz --location $URL \  
&& curl --output phpMyAdmin.tar.gz.asc --location $URL.asc \  
&& gpgv --keyring /tmp/phpmyadmin.keyring phpMyAdmin.tar.gz.asc
phpMyAdmin.tar.gz \  
&& rm -rf "$GNUPGHOME" \  
&& tar xzf phpMyAdmin.tar.gz \  
&& rm -f phpMyAdmin.tar.gz phpMyAdmin.tar.gz.asc \  
&& mv phpMyAdmin-$VERSION-all-languages /var/www/pma.dev \  
&& rm -rf /var/www/pma.dev/js/jquery/src/ /var/www/pma.dev/js/openlayers/src/
/var/www/pma.dev/setup/ /var/www/pma.dev/sql/ /var/www/pma.dev/examples/
/var/www/pma.dev/test/ /var/www/pma.dev/po/ \  
&& chown -R www-data:www-data /var/www/pma.dev \  
&& find /var/www/pma.dev -type d -exec chmod 750 {} \; \  
&& find /var/www/pma.dev -type f -exec chmod 640 {} \;  
  
COPY config.inc.php /var/www/pma.dev/  
# Copy main script  
COPY run.sh /var/www/pma.dev/run.sh  
RUN chmod u+rwx /var/www/pma.dev/run.sh  
  
RUN /var/www/pma.dev/run.sh  
  
#RUN set -x \  
# && curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz" \  
# && echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
## upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
# && tar -xzf wordpress.tar.gz -C /usr/src/ \  
# && rm wordpress.tar.gz \  
# && chown -R www-data:www-data /usr/src/wordpress  
COPY docker-entrypoint.sh /usr/local/bin/  
# RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards
compat  
# ENTRYPOINT resets CMD  
# ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  


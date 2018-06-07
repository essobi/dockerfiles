FROM php:7.1-fpm  
MAINTAINER it@digitalgarden.com.au  
  
ENV DRUPAL_DEPS_BUILD \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libpq-dev  
  
ENV DRUPAL_DEPS_RUN \  
ca-certificates \  
libjpeg62-turbo \  
libpq5 \  
mysql-client \  
ssmtp \  
wget  
  
# Create 'app' user.  
RUN groupadd --gid 1000 app \  
&& useradd --uid 1000 --gid app --shell /bin/bash --create-home app \  
&& mkdir -p /home/app/bin \  
&& mkdir -p /home/app/.local/bin \  
&& mkdir -p /home/app/.local/opt \  
&& mkdir -p /home/app/src/docroot \  
&& echo 'PATH=$HOME/bin:$PATH' >> /home/app/.bashrc \  
&& echo 'PATH=$HOME/src/docroot/vendor/bin:$PATH' >> /home/app/.bashrc \  
&& echo 'PATH=$HOME/.local/bin:$PATH' >> /home/app/.bashrc \  
&& chown -R app:app /home/app  
  
# Switch PHP-FPM user to 'app'.  
RUN sed -i 's/www-data/app/g' /usr/local/etc/php-fpm.d/www.conf  
  
# Add vendor binaries to path.  
RUN echo 'PATH=$HOME/src/docroot/vendor/bin:$PATH' >> /home/app/.bashrc \  
&& chown -R app:app /home/app  
  
# Add Drupal script.  
COPY bin/ /home/app/.local/bin/  
  
WORKDIR /home/app/src/docroot  
# Build PHP dependencies.  
RUN set -ex \  
# Add build dependencies. \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
$DRUPAL_DEPS_RUN \  
$DRUPAL_DEPS_BUILD \  
&& rm -rf /var/lib/apt/lists/* \  
# Configure 'gd' PHP extension. \  
&& docker-php-ext-configure gd \  
\--with-jpeg-dir=/usr \  
\--with-png-dir=/usr \  
# Build PHP extensions. \  
&& docker-php-ext-install -j "$(nproc)" \  
gd \  
mbstring \  
opcache \  
pdo \  
pdo_mysql \  
zip \  
# Remove build depdendencies. \  
&& apt-get purge -y --auto-remove $DRUPAL_DEPS_BUILD  
  
# Get PHP development configuration.  
RUN wget -O /usr/local/etc/php.ini https://raw.githubusercontent.com/php/php-
src/PHP-$PHP_VERSION/php.ini-development  
# Set recommended opcache.ini settings.  
# See https://secure.php.net/manual/en/opcache.installation.php.  
COPY opcache-recommended.ini /usr/local/etc/php/conf.d/opcache-recommended.ini  
# Install Xdebug extension.  
COPY xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends $PHPIZE_DEPS \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl channel-update pecl.php.net \  
&& pecl install xdebug \  
&& apt-get purge -y --auto-remove $PHPIZE_DEPS  
# Set sendmail to mail:1025 (host:port).  
# Used for linking mail containers.  
RUN echo "sendmail_path = /usr/sbin/sendmail -S mail:1025" >>
/usr/local/etc/php.ini  
# Install composer to 'app' user.  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --filename=composer --install-dir=/home/app/bin \  
&& php -r "unlink('composer-setup.php');"  


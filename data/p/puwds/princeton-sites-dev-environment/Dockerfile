# from https://www.drupal.org/docs/8/system-requirements/drupal-8-php-
requirements  
FROM php:7.1-apache  
  
RUN apt-get clean && apt-get update && apt-get install -y locales  
  
# Among other things, ensure that UTF characters in a PPA name don't break
things.  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Install packages.  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qq -o Dpkg::Options::="--force-
confold" install \  
git \  
libbz2-dev \  
libnss3 \  
libxi6 \  
mysql-client \  
ssh \  
unzip \  
vim \  
wget \  
zip && \  
apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
# Install xdebug.  
RUN pecl install xdebug  
#RUN docker-php-ext-enable xdebug  
# Copy our config into place.  
COPY etc /etc/  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
if command -v a2enmod; then \  
a2enmod rewrite; \  
fi; \  
if command -v a2enmod; then \  
a2enmod ssl; \  
fi; \  
\  
if command -v a2ensite; then \  
a2ensite default-ssl.conf; \  
fi; \  
\  
savedAptMark="$(apt-mark showmanual)"; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libjpeg-dev \  
libpng-dev \  
libpq-dev \  
; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install -j "$(nproc)" \  
bz2 \  
gd \  
opcache \  
pdo_mysql \  
pdo_pgsql \  
zip \  
; \  
\  
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all
build dependencies  
apt-mark auto '.*' > /dev/null; \  
apt-mark manual $savedAptMark; \  
ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \  
| awk '/=>/ { print $3 }' \  
| sort -u \  
| xargs -r dpkg-query -S \  
| cut -d: -f1 \  
| sort -u \  
| xargs -rt apt-mark manual; \  
\  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false;
\  
rm -rf /var/lib/apt/lists/*  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# Install Composer.  
RUN curl --silent --output /tmp/composer-setup.php
https://getcomposer.org/installer && \  
php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
&& \  
rm /tmp/composer-setup.php  
  
# Make drush and other applications easier to use.  
ENV PATH "$PATH:/var/www/html/princeton/vendor/bin"  
# Install Google Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' && \  
apt-get -y update && \  
apt-get -y install google-chrome-stable  
  
# Install ChromeDriver  
RUN LATEST_CHROMEDRIVER=$(wget -q -O -
http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \  
wget -N
http://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER/chromedriver_linux64.zip
&& \  
unzip chromedriver_linux64.zip && \  
chmod +x chromedriver && \  
mv -f chromedriver /usr/local/bin && \  
rm chromedriver_linux64.zip  
  
# Set defaults for Apache and PHP.  
ENV APACHE_RUN_USER=www-data APACHE_RUN_GROUP=www-data  
  
# Allow Xdebug to be triggered from the CLI inside the container.  
ENV XDEBUG_SESSION_START='PHPSTORM'  
ENV XDEBUG_CONFIG='idekey=PHPSTORM'  
RUN mkdir /var/www/html/princeton  
  
WORKDIR /var/www/html/princeton  
  
RUN chown -R $APACHE_RUN_USER:$APACHE_RUN_GROUP /var/www/html/princeton  
  
# Expose a volume to tooling that looks for it.  
VOLUME /var/www/html/princeton  


# Akeneo PHP  
FROM debian:stretch  
LABEL maintainer="s7b4 <baron.stephane@gmail.com>"  
  
# Base + Akeneo requirements  
RUN apt-get update \  
&& apt-get install --no-install-recommends --yes --quiet \  
apt-transport-https \  
lsb-release \  
ca-certificates \  
curl \  
gnupg2 \  
unzip \  
git \  
&& curl -sS https://packages.sury.org/php/apt.gpg | apt-key add - \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list \  
&& curl -sS https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- \  
&& echo "deb https://deb.nodesource.com/node_8.x/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/nodesource.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --yes --quiet \  
php7.1-cli \  
php7.1-fpm \  
php7.1-apcu \  
php7.1-bcmath \  
php7.1-curl \  
php7.1-gd \  
php7.1-intl \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-soap \  
php7.1-xml \  
php7.1-zip \  
php-imagick \  
nodejs \  
yarn \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/www/html/*  
  
# Config  
COPY resources/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf  
COPY resources/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
COPY resources/php_fpm.ini /etc/php/7.1/fpm/php.ini  
COPY resources/php_cli.ini /etc/php/7.1/cli/php.ini  
COPY resources/apcu.ini /etc/php/7.1/mods-available/apcu.ini  
  
# Composer  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');" \  
&& php -f /tmp/composer-setup.php -- --quiet --filename=composer --install-
dir=/usr/local/bin \  
&& rm /tmp/composer-setup.php  
  
# Scripts  
RUN mkdir /opt/cron-scripts  
COPY resources/*.sh /opt/  
COPY resources/cron-scripts /opt/cron-scripts  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
  
VOLUME /var/www/html  
  
CMD ["php-fpm7.1"]  
  
EXPOSE 9000


FROM php:7.0-apache  
  
ENV MOODLE_VERSION=v3.5.0 \  
MOODLE_GITHUB=https://github.com/moodle/moodle.git \  
MOODLE_DESTINATION=/var/www/html  
  
RUN apt-get update \  
&& apt-get install -y lsb-release \  
&& apt-get install -y libpng12-dev libjpeg-dev libpq-dev \  
graphviz aspell libpspell-dev git-core \  
&& apt-get install -y libicu-dev libxml2-dev libcurl4-openssl-dev \  
libldap2-dev \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install intl pdo mysqli xmlrpc curl pspell \  
ldap zip pgsql gd opcache soap \  
&& docker-php-ext-enable opcache \  
&& apt-get clean && rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer &&\  
/usr/local/bin/composer self-update  
  
RUN pecl install redis-3.1.0 \  
&& docker-php-ext-enable redis  
  
RUN apt-get update \  
&& apt-get install -y libmemcached-dev \  
&& yes yes | pecl install memcached \  
&& docker-php-ext-enable memcached \  
&& apt-get clean && rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*  
  
RUN git clone git://github.com/tmuras/moosh.git /usr/local/moosh-online &&\  
cd /usr/local/moosh-online && composer install && \  
ln -s /usr/local/moosh-online/moosh.php /usr/local/bin/moosh  
  
RUN git clone -b ${MOODLE_VERSION} \--depth 1 ${MOODLE_GITHUB}
${MOODLE_DESTINATION}  
RUN mkdir -p /var/moodledata/local/cache && \  
mkdir -p /var/moodledata/shared/cache && \  
mkdir -p /var/moodledata/shared/temp && \  
mkdir -p /var/moodledata/shared/dataroot && \  
chown -R www-data:www-data /var/moodledata && \  
ln -sf /var/moodlecfg/config.php ${MOODLE_DESTINATION}/config.php  
  
# Enable mod_rewrite  
RUN a2enmod rewrite  
  
COPY rootfs /


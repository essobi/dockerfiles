FROM php:7.1.5-fpm  
  
MAINTAINER Andreas Krüger <ak@patientsky.com>  
  
ENV composer_hash
669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >
/etc/apt/sources.list.d/nginx.list && \  
echo "deb-src http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list.d/nginx.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62  
  
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee
/etc/apt/sources.list.d/newrelic.list && \  
curl https://download.newrelic.com/548C16BF.gpg | apt-key add -  
  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends --no-install-suggests \  
wget \  
host \  
net-tools \  
tzdata \  
ca-certificates \  
supervisor \  
nginx \  
libmcrypt-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libcurl4-openssl-dev \  
libmagickwand-dev \  
libmagickcore-dev \  
libssl-dev \  
librabbitmq-dev \  
zlib1g-dev \  
libicu-dev \  
g++ \  
localepurge \  
make \  
unzip \  
locales \  
pkg-config \  
newrelic-php5 \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-configure pcntl \  
&& docker-php-ext-install -j$(nproc) \  
iconv \  
mcrypt \  
gd \  
pdo_mysql \  
json \  
bcmath \  
intl \  
opcache \  
mbstring \  
xml \  
zip \  
pcntl \  
&& pecl install \  
redis \  
amqp \  
igbinary \  
mongodb \  
imagick \  
&& docker-php-ext-enable \  
redis \  
amqp \  
igbinary \  
imagick \  
mongodb  
  
# Install no locale  
RUN sed -i 's/# nb_NO.UTF-8 UTF-8/nb_NO.UTF-8 UTF-8/' /etc/locale.gen \  
&& locale-gen nb_NO.UTF-8  
  
RUN sed -i "s|USE_DPKG|#USE_DPKG|" /etc/locale.nopurge && localepurge  
  
RUN apt-get purge -y \  
g++ \  
make \  
pkg-config \  
localepurge \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
RUN mkdir -p /etc/nginx && \  
mkdir -p /var/www/app && \  
mkdir -p /run/nginx && \  
mkdir -p /var/log/supervisor && \  
rm -Rf /etc/nginx/nginx.conf && \  
mkdir -p /etc/nginx/sites-enabled/ && \  
rm -Rf /etc/nginx/sites-enabled/* && \  
rm -Rf /var/www/* && \  
mkdir /var/www/html/  
  
# Setup nginx and supervisord  
ADD conf/supervisord.conf /etc/supervisord.conf  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/nginx-site.conf /etc/nginx/sites-enabled/default.conf  
  
# tweak php-fpm  
RUN rm /usr/local/etc/php-fpm.d/*  
ADD conf/php-fpm.conf /usr/local/etc/php-fpm.d/php-fpm.conf  
ADD conf/www.conf /usr/local/etc/php-fpm.d/www.conf  
  
# tweak php  
ADD conf/php.ini /usr/local/etc/php/php.ini  
  
# Configure php opcode cache  
RUN echo
"opcache.enable=1\nopcache.enable_cli=1\nopcache.consistency_checks=0\nopcache.file_cache=/tmp\nopcache.file_cache_consistency_checks=0\nopcache.validate_timestamps=0\nopcache.max_accelerated_files=32531\nopcache.memory_consumption=512\nopcache.interned_strings_buffer=8\nopcache.revalidate_freq=60\nopcache.fast_shutdown=0\nopcache.error_log=/proc/self/fd/2"
>> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini  
RUN echo "<?php var_dump(opcache_get_status(false)); phpinfo();" >
/var/www/phpinfo.php  
  
# Add errors and scripts  
ADD errors/ /var/www/errors  
ADD scripts/start.sh /start.sh  
ADD scripts/setup.sh /setup.sh  
RUN chmod 755 /start.sh && \  
chmod 755 /setup.sh  
  
# Add composer  
RUN composer_hash=$(wget -q -O - https://composer.github.io/installer.sig) &&
\  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') === '${composer_hash}')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  
# Add tini  
ENV TINI_VERSION v0.14.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc
/tini.asc  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
&& gpg --verify /tini.asc  
RUN chmod +x /tini  
  
EXPOSE 80  
CMD ["/start.sh"]  


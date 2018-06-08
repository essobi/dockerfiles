FROM php:7-fpm-alpine  
  
RUN apk update --no-cache && apk upgrade --no-cache  
  
RUN apk add --no-cache \  
acl \  
git \  
wget \  
zip \  
unzip \  
gzip \  
tar \  
bash \  
openssl-dev \  
pcre-dev \  
freetype-dev \  
gd-dev \  
libmcrypt-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
zlib-dev \  
&& rm -rf /var/cache/apk/*  
  
#Configure and build PHP  
RUN docker-php-ext-install mcrypt \  
&& docker-php-ext-configure gd --with-png-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mbstring  
  
#Build Predis  
RUN git clone https://github.com/phpredis/phpredis.git /tmp/phpredis \  
&& cd /tmp/phpredis \  
&& git checkout php7 \  
&& phpize \  
&& ./configure \  
&& make \  
&& make test \  
&& make install \  
&& make clean \  
&& cd .. \  
&& rm -rf phpredis \  
&& echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini  
  
#Install New Relic PHP agent  
ENV NR_INSTALL_SILENT=true \  
NR_INSTALL_KEY=61ad08973c48a9bc61ce925de82a63eb4941acf4 \  
NR_INSTALL_USE_CP_NOT_LN=true \  
NR_VERSION_INSTALL=6.2.0.158  
# NR_INSTALL_PHPLIST=/usr/local/bin/php  
RUN cd /tmp \  
&& wget -nv -O- https://download.newrelic.com/php_agent/release/newrelic-
php5-$NR_VERSION_INSTALL-linux.tar.gz | gzip -dc | tar x > newrelic-
php5-$NR_VERSION_INSTALL-linux \  
&& cd /tmp/newrelic-php5-$NR_VERSION_INSTALL-linux \  
&& ./newrelic-install install \  
&& cd /tmp \  
&& rm -R newrelic-php5-$NR_VERSION_INSTALL-linux  
  
  
COPY php-fpm.conf /usr/local/etc/  
ADD php-fpm.d/* /usr/local/etc/php-fpm.d/  
  
ADD conf.d/date.ini /usr/local/etc/php/conf.d/date.ini  
  
#Delete unused deps  
#RUN apk del \  
# git \  
# wget \  
# gzip \  
# tar  
RUN mkdir -p /root/.ssh \  
&& echo "Host github.com\n\tStrictHostKeyChecking no\nHost
bitbucket.org\n\tStrictHostKeyChecking no" >> /root/.ssh/config \  
&& chown -R root:root /root/.ssh \  
&& chmod -R go-rwx /root/.ssh  
  
  
  
EXPOSE 9000  
CMD ["php-fpm"]  
  
# CMD ["/usr/sbin/php5-fpm", "--nodaemonize", "--fpm-config /etc/php5/fpm/php-
fpm.conf"]  


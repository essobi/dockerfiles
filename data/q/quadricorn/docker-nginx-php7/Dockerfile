FROM mcuyar/docker-alpine-nginx  
MAINTAINER Matthew Cuyar <matt@enctypeapparel.com>  
  
##/  
# Install PHP  
#/  
RUN apk --no-cache --update add \  
php5 \  
php5-fpm \  
php5-xml \  
php5-pgsql \  
php5-mysqli \  
php5-pdo_mysql \  
php5-mcrypt \  
php5-opcache \  
php5-gd \  
php5-curl \  
php5-json \  
php5-phar \  
php5-openssl \  
php5-ctype \  
php5-zip \  
php5-dom \  
pdftk \  
curl  
  
##/  
# Install composer  
#/  
ENV COMPOSER_HOME=/composer  
RUN mkdir /composer \  
&& curl -sS https://getcomposer.org/installer | php5 \  
&& mkdir -p /opt/composer \  
&& mv composer.phar /opt/composer/composer.phar  
  
##/  
# Install New Relic PHP Agent  
#/  
RUN mkdir /tmp/newrelic \  
&& cd /tmp/newrelic \  
&& wget "http://download.newrelic.com/php_agent/release/$(curl
http://download.newrelic.com/php_agent/release/ | grep -ohE 'newrelic-
php5-.*?-linux-musl.tar.gz' | cut -f1 -d\")" -O php-agent.tar.gz \  
&& gzip -dc php-agent.tar.gz | tar xf - \  
&& mkdir -p /opt/newrelic \  
&& cp -a "$(ls | grep 'newrelic')/." /opt/newrelic/ \  
&& rm -rf /tmp/newrelic  
  
##/  
# Set the work directory  
#/  
WORKDIR /var/www  
  
##/  
# Copy files  
#/  
COPY rootfs /


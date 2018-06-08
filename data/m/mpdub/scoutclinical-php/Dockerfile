FROM php:5.6.31-fpm-alpine  
  
ARG GIT_COMMIT=unknown  
ARG BUILD_DATE=unknown  
  
LABEL com.scoutclinical.php "php 5.6.31 alpine"  
LABEL org.label-schema.cmd "docker run -d -p 9000:9000"  
LABEL org.label-schema.name "Scout PHP"  
LABEL org.label-schema.vendor "Meeting Protocol Worldwide"  
LABEL maintainer "Darren Green <darren.green@meetingprotocol.com>"  
  
RUN apk add --no-cache --update \  
autoconf \  
g++ \  
icu-dev \  
libmcrypt-dev \  
libxml2 \  
libxml2-dev \  
make \  
openssl-dev \  
&& docker-php-ext-install \  
intl \  
mcrypt \  
soap \  
&& pecl install \  
mongo-1.6.14 \  
xdebug-2.5.0 \  
&& docker-php-ext-enable \  
mongo \  
xdebug \  
&& printf "%s\n" \  
"catch_workers_output = yes" \  
"php_flag[display_errors] = on" \  
"php_admin_flag[log_errors] = on" \  
>> /usr/local/etc/php-fpm.d/www.conf \  
&& printf "%s\n" \  
"date.timezone = \"America/Chicago\"" \  
>> /usr/local/etc/php/conf.d/timezone.ini  
  
WORKDIR /var/www/scoutclinical  
  
LABEL org.label-schema.build-date $BUILD_DATE  
LABEL org.label-schema.vcs-ref $GIT_COMMIT  


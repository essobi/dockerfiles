FROM alpine:latest as builder  
RUN apk add --update \  
openssl \  
wget \  
&& wget -U "" https://www.milchundzucker.de/ROOT-CA.crt
https://www.milchundzucker.de/milchundzucker-ca.crt \  
&& openssl x509 -inform DER -outform PEM -in ROOT-CA.crt -out ROOT-CA.crt \  
&& openssl x509 -inform DER -outform PEM -in milchundzucker-ca.crt -out
milchundzucker-ca.crt \  
&& rm -rf /var/cache/apk/*  
  
FROM php:7.2  
LABEL maintainer="jens.kohl@milchundzucker.de"  
  
ENV COMPOSER_CACHE_DIR /cache/composer  
ENV YARN_CACHE_FOLDER /cache/yarn  
ENV NPM_CONFIG_CACHE /cache/npm  
ENV bower_storage__packages /cache/bower  
ENV GEM_SPEC_CACHE /cache/gem  
ENV PIP_DOWNLOAD_CACHE /cache/pip  
  
COPY \--from=builder /ROOT-CA.crt /usr/local/share/ca-certificates/ROOT-CA.crt  
COPY \--from=builder /milchundzucker-ca.crt /usr/local/share/ca-
certificates/milchundzucker-ca.crt  
  
COPY \--from=composer:latest /usr/bin/composer /usr/local/bin/composer  
COPY \--from=milchundzucker/php-parallel-lint:latest /usr/local/bin/parallel-
lint /usr/local/bin/parallel-lint  
  
COPY assets/ssh_config /root/.ssh/config  
COPY assets/uopz /usr/local/bin/uopz  
COPY assets/xdebug /usr/local/bin/xdebug  
  
RUN apt-get update && apt-get install -y \  
git-core \  
subversion \  
unzip \  
rsync \  
ssh-client \  
libxml2-dev \  
libssh2-1-dev \  
libicu-dev \  
libbz2-dev \  
libzip-dev \  
libgmp3-dev \  
\--no-install-recommends && apt-get clean  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
  
RUN set -xe \  
&& update-ca-certificates \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
${PHP_INI_DIR}/conf.d/date_timezone.ini \  
&& php -v \  
&& mkdir -p /composer \  
&& curl -fsS https://composer.github.io/snapshots.pub -o
/composer/keys.dev.pub \  
&& curl -fsS https://composer.github.io/releases.pub -o
/composer/keys.tags.pub \  
&& cd /tmp \  
&& composer global require hirak/prestissimo \  
&& curl -L http://www.phing.info/get/phing-latest.phar -o /usr/local/bin/phing
--silent \  
&& chmod +x /usr/local/bin/phing \  
&& which phing \  
&& phing -version \  
&& pecl install uopz-5.0.2 \  
&& chmod +x /usr/local/bin/uopz \  
&& echo "extension=uopz.so" > ${PHP_INI_DIR}/conf.d/uopz.ini \  
&& pecl install ssh2-1.1.2 \  
&& echo "extension=ssh2.so" > ${PHP_INI_DIR}/conf.d/ssh2.ini \  
&& docker-php-ext-install opcache soap pdo_mysql intl bz2 gmp sockets zip  
  
RUN pecl install xdebug \  
&& chmod +x /usr/local/bin/xdebug \  
&& php -m  
# && echo "zend_extension=xdebug.so" > ${PHP_INI_DIR}/conf.d/xdebug.ini  
RUN cat $HOME/.ssh/config && chmod -R 600 $HOME/.ssh && ls -l
$HOME/.ssh/config  
  
CMD php -a  


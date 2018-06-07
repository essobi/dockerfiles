FROM alpine:edge  
  
MAINTAINER Sam Mousa <sam@mousa.nl>  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk add --update --no-cache \  
tini \  
curl \  
git \  
openssh-client \  
poppler-utils \  
php7 \  
php7-sockets \  
php7-xml \  
php7-xmlreader \  
php7-pdo_mysql \  
php7-intl \  
php7-sockets \  
php7-pcntl \  
php7-zip \  
php7-json \  
php7-phar \  
php7-dom \  
php7-mbstring \  
php7-zlib \  
php7-ctype \  
php7-pcntl \  
php7-curl \  
php7-mcrypt \  
php7-xmlwriter \  
php7-session \  
php7-posix \  
php7-pdo_sqlite \  
php7-pdo \  
php7-soap \  
php7-gd \  
php7-fileinfo \  
php7-iconv  
  
  
  
# Add php.ini directives.  
RUN echo memory_limit=1G > /etc/php7/php.ini  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/bin
--filename=composer && \  
composer global config bin-dir /bin && \  
composer global config vendor-dir /vendor  
  
# fxp/composer-asset-plugin && codeception  
RUN composer -n global require fxp/composer-asset-plugin
codeception/codeception redcomponent/teststatistics && \  
composer clear-cache  
  
# Install php wait-for-it  
RUN cd /tmp && \  
git clone --branch v0.6.0 https://github.com/SAM-IT/wait-for-it-php.git && \  
cd wait-for-it-php && \  
composer install && \  
php -d phar.readonly=0 build.php && \  
cp wait-for-it.phar /bin/wait-for-it && \  
rm -rf /tmp/*  
  
WORKDIR /project  


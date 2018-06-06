#  
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
FROM php:7.1-alpine  
  
# Install ext-zip  
RUN apk add --update --no-cache --virtual=.ext-zip-deps \  
coreutils \  
zlib-dev \  
&& docker-php-ext-install -j$(nproc) zip \  
&& apk del .ext-zip-deps  
  
# Install composer dependencies  
RUN apk add --update --no-cache --virtual=.composer-deps \  
git \  
subversion  
  
# Memory Limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
# Time Zone  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
# Register the COMPOSER_HOME environment variable  
ENV COMPOSER_HOME /composer  
  
# Add global binary directory to PATH and make sure to re-export it  
ENV PATH /composer/vendor/bin:$PATH  
  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
# Composer install (https://getcomposer.org/doc/faqs/how-to-install-composer-
programmatically.md)  
RUN set -xe; \  
\  
php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');"; \  
ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', '/tmp/composer-
setup.php');"); \  
\  
if [ "$ACTUAL_SIGNATURE" !=
"55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30"
]; then \  
>&2 echo 'ERROR: Invalid installer signature'; \  
exit 1; \  
fi; \  
\  
php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
--version="1.3.2"; \  
rm /tmp/composer-setup.php  
  
# Install prestissimo  
RUN composer global require "hirak/prestissimo:^0.3"  
  
# Set up the volumes and working directory  
VOLUME ["/app"]  
WORKDIR /app  
  
# Set entrypoint  
ENTRYPOINT ["composer"]  
  


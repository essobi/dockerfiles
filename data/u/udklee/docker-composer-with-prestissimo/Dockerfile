#  
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
FROM php:7.2  
# Install ext-zip  
RUN apt-get update && apt-get install -y --no-install-recommends \  
zlib1g-dev \  
&& docker-php-ext-install -j$(nproc) zip \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# Install composer dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git \  
subversion \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
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
"544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061"
]; then \  
>&2 echo 'ERROR: Invalid installer signature'; \  
exit 1; \  
fi; \  
\  
php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
--version="1.6.2"; \  
rm /tmp/composer-setup.php  
  
# Install prestissimo  
RUN composer global require "hirak/prestissimo:^0.3"  
  
# Set up the volumes and working directory  
VOLUME ["/app"]  
WORKDIR /app  
  
# Set entrypoint  
ENTRYPOINT ["composer"]  
  


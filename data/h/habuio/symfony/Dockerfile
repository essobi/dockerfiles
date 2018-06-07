FROM php:7.1-fpm  
MAINTAINER Ruben Knol <c.minor6@gmail.com>  
  
# Set the Symfony environment, default to development/debug  
ONBUILD ARG SYMFONY_ENV=dev  
  
# install requirements  
RUN apt-get update \  
&& apt-get install -y libcurl4-openssl-dev libssl-dev libsasl2-dev libmcrypt-
dev \  
curl git unzip --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install -j$(nproc) mcrypt pdo pdo_mysql  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Copy our custom php.ini settings optimized for Symfony 3  
COPY ./php.ini /usr/local/etc/php/conf.d/99-custom.ini  
  
# Copy the project into the image  
WORKDIR /usr/app  
RUN mkdir -p /usr/app /usr/app/vendor  
ONBUILD COPY . /usr/app/  
  
# Remove any pre-existing cache just to be sure  
ONBUILD RUN rm -rf var/cache/* var/logs/* var/sessions/* vendor/*  
  
# Install dependencies depending on environment context  
# Note: bash needs to be installed on the imagex  
ONBUILD RUN bash -c "[ \"$SYMFONY_ENV\" == \"prod\" ] \  
&& composer install --no-interaction --no-dev \  
|| composer install --no-interaction"  
  
# Run the cache warmer to generate  
ONBUILD RUN php bin/console cache:warmup --env=$SYMFONY_ENV  
  
# Set the appropriate permissions for php-fpm to write to
logs/cache/sessions/vendor  
ONBUILD RUN chown -R www-data var/cache var/logs var/sessions vendor  
  
# Depending on the Symfony environment mode, delete app.php or app_dev.php  
ONBUILD RUN bash -c "[ \"$SYMFONY_ENV\" == \"prod\" ] && rm web/app_dev.php ||
rm web/app.php"  
  
EXPOSE 9000


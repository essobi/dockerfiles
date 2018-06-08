FROM php:7.0-fpm  
MAINTAINER Daniel Louvier <daniel.louvier@movingimage.com>  
  
# Set the timezone.  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
# Set the Symfony environment, default to development/debug  
ONBUILD ARG SYMFONY_ENV=dev  
  
# Copy our custom php.ini settings optimized for Symfony 3  
COPY ./php.ini /usr/local/etc/php/conf.d/99-custom.ini  
  
# Add nodejs repo  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash && apt-get update &&
\  
apt-get install -y --no-install-recommends libcurl4-openssl-dev libssl-dev \  
libsasl2-dev libmcrypt-dev curl git unzip nodejs && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-install -j$(nproc) mcrypt && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
# Copy the project into the image  
WORKDIR /var/www  
  
# Prepare directories  
RUN mkdir /var/www/vendor  
  
ONBUILD COPY . /var/www/  
  
ONBUILD RUN rm -rf var/{cache,logs,sessions}/* vendor/* node_modules/* && \  
usermod -s /bin/bash www-data && \  
chown -R www-data . && \  
su www-data -c 'npm install' && \  
su www-data -c 'bash -c "[ \"$SYMFONY_ENV\" == \"prod\" ] \  
&& composer install --no-interaction --no-dev \  
|| composer install --no-interaction"' && \  
su www-data -c 'php bin/console cache:warmup --env=$SYMFONY_ENV' && \  
su www-data -c 'bash -c "[ \"$SYMFONY_ENV\" == \"prod\" ] \  
&& rm web/app_dev.php || rm web/app.php"' && \  
usermod -s /bin/nologin www-data  
EXPOSE 9000  


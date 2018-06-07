FROM php:7.0-apache  
MAINTAINER ignacio@introbay.com  
  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev
git zip mysql-client bundler \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql zip \  
&& docker-php-ext-install opcache \  
&& pecl install redis-3.0.0 \  
&& docker-php-ext-enable redis \  
&& a2enmod rewrite \  
&& rm -rf /var/lib/apt/lists/*  
  
# Compile and install uploadprogress #  
RUN git clone https://github.com/Jan-E/uploadprogress.git /tmp/php-
uploadprogress \  
&& cd /tmp/php-uploadprogress \  
&& phpize \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install \  
&& echo 'extension=uploadprogress.so' > $PHP_INI_DIR/conf.d/uploadprogress.ini
\  
&& rm -rf /tmp/*  
  
COPY drupal-*.ini /usr/local/etc/php/conf.d/  
  
# Install drush by using composer  
ENV COMPOSER_HOME /root/composer  
ENV COMPOSER_VERSION master  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer global require drush/drush:8.* \  
&& ln -sf $COMPOSER_HOME/vendor/bin/drush.php /usr/local/bin/drush \  
&& drush cache-clear drush  


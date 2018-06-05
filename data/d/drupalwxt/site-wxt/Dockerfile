FROM drupalcomposer/drupal  
MAINTAINER William Hearn <sylus1984@gmail.com>  
  
# Allow Composer to be run as root.  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_VERSION 1.4.2  
# Setup the Composer installer.  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
  
# Install Composer.  
RUN php /tmp/composer-setup.php --no-ansi \  
\--install-dir=/usr/local/bin \  
\--filename=composer \  
\--version=${COMPOSER_VERSION} && \  
rm -rf /tmp/composer-setup.php  
  
# Install Drupal via composer.  
RUN rm -f /var/www/composer.lock && \  
rm -rf /root/.composer  
  
COPY scripts/ScriptHandler.php /var/www/scripts/ScriptHandler.php  
COPY composer.json /var/www/composer.json  
WORKDIR /var/www  
RUN composer global require "hirak/prestissimo:^0.3" && \  
composer install --prefer-dist \  
\--no-interaction \  
\--no-dev  
  
# Permissions.  
WORKDIR /var/www/html  
RUN chown -R www-data:www-data *  
  
# Drush.  
RUN ln -s /var/www/vendor/drush/drush/drush /usr/local/bin/drush  
  
RUN php -r 'opcache_reset();'  
  
# See: https://github.com/docker/docker/issues/9299  
RUN echo "export TERM=xterm" >> ~/.bashrc  


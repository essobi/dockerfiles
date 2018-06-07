FROM php:5.6-apache  
  
# Apache configuration  
RUN a2enmod rewrite  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Install the PHP extensions we need.  
RUN apt-get update && apt-get install -y git libpng12-dev libjpeg-dev libpq-
dev mariadb-client-core-10.0 \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring opcache pdo pdo_mysql pdo_pgsql zip  
  
# Adding custom PHP settings.  
COPY php.ini /usr/local/etc/php/conf.d/drupal.ini  
  
# Install uploadprogress extension.  
RUN pecl install uploadprogress \  
&& echo "extension=uploadprogress.so" >>
/usr/local/etc/php/conf.d/uploadprogress.ini \  
&& rm -vrf /tmp/pear  
  
# Install Twig C extension.  
ENV TWIG_VERSION 1.22.3  
ENV TWIG_MD5 41245d409760a0a1d27108a5470e2f6f  
RUN mkdir /tmp/twig && cd /tmp/twig \  
&& curl -fSL "https://github.com/twigphp/Twig/archive/v${TWIG_VERSION}.tar.gz"
-o twig.tar.gz \  
&& echo "${TWIG_MD5} *twig.tar.gz" | md5sum -c - \  
&& tar -xz --strip-components=1 -f twig.tar.gz \  
&& rm twig.tar.gz \  
&& cd ext/twig && phpize \  
&& ./configure && make && make install \  
&& cp /tmp/twig/ext/twig/modules/twig.so $(php-config --extension-dir) \  
&& echo "extension=twig.so" > /usr/local/etc/php/conf.d/twig.ini \  
&& cd /tmp && rm -vrf /tmp/twig  
  
# Install Drush using Composer.  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer global require drush/drush:dev-master  
RUN ln -sf $HOME/.composer/vendor/bin/drush /usr/local/bin/drush  
RUN drush --version  
  
# Set user 1000 and group staff to www-data, enables write permission.  
# https://github.com/boot2docker/boot2docker/issues/581#issuecomment-114804894  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
  
WORKDIR /var/www/html  
  
# Install Drupal  
ENV DRUPAL_VERSION 8.0.0  
RUN drush dl drupal-${DRUPAL_VERSION} -d --destination=".." \--drupal-project-
rename="$(basename `pwd`)" -y  
RUN chown -R www-data:www-data .  
  
VOLUME ["/var/www/html"]  


FROM eugeneware/php-5.3:master  
MAINTAINER Craig Gardener <craiggardener.me@gmail.com>  
  
# This Dockerfile is used to build the "drupal" Docker image.  
# Enable Apache2 extensions  
RUN a2enmod rewrite  
  
# Install PHP extensions  
RUN apt-get update \  
&& apt-get install -y libpng12-dev libjpeg-dev libpq-dev libxml2-dev \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir -p /usr/local/etc/php/conf.d/ \  
&& touch /usr/local/etc/php/conf.d/docker-php-ext-gd.ini \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql soap zip  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y curl git mysql-client rsync \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> ~/.bashrc \  
&& . ~/.bashrc \  
&& composer --version  
  
# Install Drush  
RUN composer global require drush/drush:7 --prefer-dist \  
&& . ~/.bashrc \  
&& ln -sf $COMPOSER_HOME/vendor/bin/drush.php /usr/local/bin/drush \  
&& drush --version \  
&& drush @none dl registry_rebuild  
  
COPY ./start /start  
RUN chmod +x /start  
  
WORKDIR /var/www/html  
CMD ["/start"]  


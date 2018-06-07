FROM drupal:8.5  
# install the PHP extensions we need  
RUN apt-get update \  
&& apt-get install -y git mariadb-client wget vim mysql-client \  
&& docker-php-ext-install mysqli \  
&& rm -rf /var/lib/apt/lists/*  
  
#  
RUN touch /usr/local/etc/php/conf.d/uploads.ini  
RUN { \  
echo 'upload_max_filesize = 100M;'; \  
echo 'post_max_size = 150M;'; \  
echo 'max_execution_time = 180;'; \  
echo 'date.timezone="UTC";'; \  
} >> /usr/local/etc/php/conf.d/uploads.ini  
  
# for commerce  
RUN docker-php-ext-install bcmath  
  
# Uploadprogress  
RUN git clone https://github.com/php/pecl-php-uploadprogress.git
/usr/src/php/ext/uploadprogress/ && \  
docker-php-ext-configure uploadprogress && \  
docker-php-ext-install uploadprogress  
  
# install Composer globally  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# install drush, from http://docs.drush.org/en/master/install/  
# RUN wget http://files.drush.org/drush.phar \  
# && chmod +x drush.phar \  
# && mv drush.phar /usr/local/bin/drush \  
# && drush init -y  
RUN composer global require drush/drush  
  
# install Drupal Console, from https://drupalconsole.com/  
RUN curl https://drupalconsole.com/installer -L -o drupal.phar \  
&& mv drupal.phar /usr/local/bin/drupal \  
&& chmod +x /usr/local/bin/drupal  
  
# download devel module  
RUN curl -fSL "https://ftp.drupal.org/files/projects/devel-8.x-1.x-dev.tar.gz"
-o devel.tar.gz \  
&& tar -xvzf devel.tar.gz \  
&& rm devel.tar.gz \  
&& mv devel modules/contrib/  
  
# install Xdebug.  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
# enable Xdebug remote debugging  
RUN { \  
echo 'xdebug.remote_enable=true'; \  
echo 'xdebug.remote_port=9001'; \  
} >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
ENV TERM xterm  


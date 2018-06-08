FROM php:5.6-apache  
  
WORKDIR /root  
  
#
https://docs.nextcloud.com/server/12/admin_manual/installation/source_installation.html#additional-
apache-configurations  
RUN a2enmod rewrite headers env dir mime remoteip  
  
#
https://docs.nextcloud.com/server/12/admin_manual/installation/source_installation.html#prerequisites-
for-manual-installation  
# Required, Database connectors, Recommended packages  
RUN apt-get update \  
&& apt-get install -y bzip2 unzip libpng-dev libzip-dev libbz2-dev libicu-dev
libmcrypt-dev libmcrypt4 \  
&& docker-php-ext-install gd zip pdo_mysql bz2 intl mcrypt opcache \  
&& apt-get remove -y libpng-dev libicu-dev libmcrypt-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# For enhanced server performance  
#RUN yes '' | pecl install apcu-4.0.11  
#RUN docker-php-ext-enable apcu  
COPY php-opcache.ini /usr/local/etc/php/conf.d/  
COPY php-sendmail.ini /usr/local/etc/php/conf.d/  
  
ARG VERSION=12.0.2  
RUN curl -s -O
https://download.nextcloud.com/server/releases/nextcloud-${VERSION}.tar.bz2 \  
&& tar -xjf nextcloud-${VERSION}.tar.bz2 -C /var/www/ \  
&& rm nextcloud-${VERSION}.tar.bz2  
  
RUN curl -s -L -O https://github.com/asannou/user_saml/archive/deactivate-
session.zip \  
&& unzip deactivate-session.zip \  
&& mv user_saml-deactivate-session /var/www/nextcloud/apps/user_saml \  
&& rm deactivate-session.zip  
  
RUN chown -R www-data:www-data /var/www/nextcloud/  
  
#
https://docs.nextcloud.com/server/12/admin_manual/installation/source_installation.html#apache-
web-server-configuration  
COPY nextcloud.conf /etc/apache2/sites-available/  
RUN ln -s /etc/apache2/sites-available/nextcloud.conf /etc/apache2/sites-
enabled/nextcloud.conf  
  
VOLUME /volume  
  
COPY config.php /root/  
COPY entrypoint.sh /root/  
ENTRYPOINT ["/root/entrypoint.sh"]  
CMD ["apache2-foreground"]  
  


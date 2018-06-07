FROM php:5.6-apache  
MAINTAINER Jonas Thiel <jonas@thiel.io>  
  
ENV ROUNDCUBE_VERSION 1.2.3  
ENV RELEASE_DATE 2017-01-19  
ENV ROUNDCUBE_DIR /var/www/html  
ENV ROUNDCUBE_PACKAGE roundcubemail-$ROUNDCUBE_VERSION  
ENV ROUNDCUBE_VARIANT $ROUNDCUBE_PACKAGE-complete  
ENV ROUNDCUBE_DOWNLOAD
https://github.com/roundcube/roundcubemail/releases/download/$ROUNDCUBE_VERSION/$ROUNDCUBE_VARIANT.tar.gz  
  
ENV TIMEZONE Europe/Berlin  
  
RUN a2enmod rewrite expires headers  
  
ENV REQUIRED_PACKAGES mysql-client libicu-dev libldap2-dev  
ENV REQUIRED_PEAR mail_mime mail_mimedecode net_smtp net_idna2-beta auth_sasl
net_sieve crypt_gpg  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
--no-install-recommends \  
$REQUIRED_PACKAGES \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /var/cache/debconf/*-old
/usr/share/doc/* /usr/share/man/* \  
&& cp -r /usr/share/locale/en\@* /tmp/ && rm -rf /usr/share/locale/* && mv
/tmp/en\@* /usr/share/locale/  
  
# Install the PHP extensions we need  
RUN docker-php-ext-configure intl \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install pdo pdo_mysql intl exif ldap  
  
# Install pear extensions  
RUN pear install $REQUIRED_PEAR \  
&& rm -rf /tmp/*  
  
# Set recommended PHP.ini settings  
COPY php.ini /usr/local/etc/php/conf.d/my_php.ini  
  
# See https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# Set timezone  
RUN { \  
echo "date.timezone=$TIMEZONE"; \  
} > /usr/local/etc/php/conf.d/date.ini  
  
WORKDIR /  
  
RUN curl -O -L $ROUNDCUBE_DOWNLOAD \  
&& tar xzf $ROUNDCUBE_VARIANT.tar.gz \  
&& rm -r $ROUNDCUBE_DIR \  
&& mv $ROUNDCUBE_PACKAGE $ROUNDCUBE_DIR \  
&& rm -rf $ROUNDCUBE_PACKAGE \  
&& echo '<?php\n$config = array();\n' > $ROUNDCUBE_DIR/config/config.inc.php \  
&& rm -fr $ROUNDCUBE_DIR/installer \  
&& mkdir -p $ROUNDCUBE_DIR/config/custom \  
&& chown -R www-data:www-data $ROUNDCUBE_DIR  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
VOLUME /var/www/html/logs /var/www/html/temp  
EXPOSE 80  
WORKDIR $ROUNDCUBE_DIR  
CMD ["app:start"]  


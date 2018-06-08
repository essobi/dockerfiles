FROM spatialy/php7  
MAINTAINER UBIQUOS <info@ubiquos.io> (@ubiquos)  
  
# Enable Apache Rewrite Module  
RUN a2enmod rewrite  
  
# Install PHP extensions  
RUN apt-get update && \  
# apt-get install -qy libc-client-dev libicu-dev libkrb5-dev libmcrypt-dev
libssl-dev unzip zip cron curl  
apt-get install -qy unzip zip cron curl  
RUN apt-get autoremove -qy --purge \  
&& \  
apt-get clean -qy && \  
rm -rf /tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
## FROM ORIGINAL  
# RUN docker-php-ext-configure imap --with-imap --with-imap-ssl --with-
kerberos  
# RUN docker-php-ext-install imap intl mbstring mcrypt mysqli pdo pdo_mysql
zip  
RUN apt-get update -qy && \  
apt-get install -qy \  
php7.0-imap \  
php7.0-intl \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-curl \  
php7.0-xml \  
php7.0-zip \  
&& \  
apt-get install -qy \  
nano \  
&& \  
apt-get autoremove -qy --purge \  
&& \  
apt-get clean -qy && \  
rm -rf /tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
VOLUME /var/www/html  
  
# Define Mautic version and expected SHA1 signature  
ENV MAUTIC_VERSION 2.5.1  
# Download package and extract to web volume  
RUN curl -o mautic.zip -SL
https://s3.amazonaws.com/mautic/releases/${MAUTIC_VERSION}.zip \  
&& mkdir /usr/src/mautic \  
&& unzip mautic.zip -d /usr/src/mautic \  
&& rm mautic.zip \  
&& chown -R www-data:www-data /usr/src/mautic  
  
# Copy init scripts and custom .htaccess  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY makeconfig.php /makeconfig.php  
COPY makedb.php /makedb.php  
  
COPY mautic.cron /etc/cron.d/mautic.cron  
RUN chmod 644 /etc/cron.d/mautic.cron  
  
RUN touch /var/log/mautic.cron.log  
RUN chmod +rw /var/log/mautic.cron.log  
  
RUN /usr/bin/crontab /etc/cron.d/mautic.cron  
  
RUN chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apachectl", "-DFOREGROUND"]  
  


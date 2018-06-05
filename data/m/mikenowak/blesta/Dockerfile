FROM php:7.0-apache  
  
RUN apt-get update \  
&& apt-get install --yes --force-yes cron g++ gettext libicu-dev openssl libc-
client-dev libkrb5-dev libxml2-dev libfreetype6-dev libgd-dev libmcrypt-dev
bzip2 libbz2-dev libtidy-dev libcurl4-openssl-dev libz-dev libmemcached-dev
libxslt-dev libgmp-dev libldap2-dev python3 python3-pycurl unzip wget
supervisor \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-configure imap \--with-kerberos --with-imap-ssl \  
&& docker-php-ext-install pdo pdo_mysql curl gmp imap json ldap mbstring
mcrypt simplexml gd \  
&& yes '' | pecl install -f mailparse \  
&& a2enmod rewrite \  
&& a2enmod headers \  
&& a2enmod remoteip \  
&& apt-get -y autoclean && apt-get -y autoremove && apt-get -y clean && rm -rf
/var/lib/apt/lists/* \  
&& rm -Rf /etc/cron.{hourly,daily,weekly,monthly} \  
&& echo "extension=mailparse.so" > /usr/local/etc/php/conf.d/docker-php-ext-
mailparse.ini \  
&& sed -i 's/^LogFormat/#&/' /etc/apache2/apache2.conf \  
&& echo "[PHP]" >> /usr/local/etc/php/php.ini \  
&& echo "expose_php=Off" >> /usr/local/etc/php/php.ini \  
&& echo "ServerTokens Prod" >> /etc/apache2/conf-enabled/security.conf \  
&& echo "ServerSignature Off" >> /etc/apache2/conf-enabled/security.conf \  
&& echo "<IfModule remoteip_module>" > /etc/apache2/conf-enabled/remoteip.conf
\  
&& echo " RemoteIPHeader X-Forwarded-For" >> /etc/apache2/conf-
enabled/remoteip.conf \  
&& echo " RemoteIPTrustedProxy 172.0.0.0/8" >> /etc/apache2/conf-
enabled/remoteip.conf \  
&& echo "</IfModule>" >> /etc/apache2/conf-enabled/remoteip.conf  
  
RUN cd /tmp \  
&& curl -o ioncube.tar.gz
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -zxf ioncube.tar.gz \  
&& mv ioncube/ioncube_loader_lin_7.0.so /usr/local/lib/php/extensions/* \  
&& rm -Rf ioncube.tar.gz ioncube \  
&& echo "zend_extension=ioncube_loader_lin_7.0.so" >
/usr/local/etc/php/conf.d/00_docker-php-ext-ioncube.ini  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
ADD logformat.conf /etc/apache2/conf-enabled/logformat.conf  
  
RUN echo '*/5 * * * * www-data /usr/local/bin/php /var/www/html/index.php
cron' > /etc/cron.d/blesta \  
&& echo '' > /etc/cron.d/geoip  
  
CMD ["/usr/bin/supervisord"]  


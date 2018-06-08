FROM php:5-apache  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCRIPT_DIR /opt  
  
# Install Apache2, PHP and LTB ssp  
RUN apt-get update && \  
apt-get install -y \  
msmtp sudo gettext-base \  
libldap2-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev && \  
apt-get clean && \  
ln -fs /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ && \  
docker-php-ext-install -j$(nproc) iconv mcrypt && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
docker-php-ext-install ldap  
  
RUN curl http://tools.ltb-project.org/attachments/download/801/self-service-
password_0.9-1_all.deb > self-service-password.deb && \  
dpkg -i --force-depends self-service-password.deb ; rm -f self-service-
password.deb  
  
# Add LSSP's Apache-config for site  
ADD ["assets/config/apache2/vhost.conf", "/etc/apache2/sites-available/self-
service-password.conf"]  
# Add LSSP's config template  
ADD ["assets/config/lssp/config.inc.php", "/usr/share/self-service-
password/conf/config.inc.php.dist"]  
# Add MSMTP's config for PHP  
ADD ["assets/config/php/php-sendmail.ini", "/usr/local/etc/php/conf.d"]  
# Add MSMTP's config  
ADD ["assets/config/msmtp/msmtprc.noauth", "/etc/msmtprc.noauth.dist"]  
ADD ["assets/config/msmtp/msmtprc.auth", "/etc/msmtprc.auth.dist"]  
  
# Enable LSSP in Apache Web-Server  
RUN a2dissite 000-default && \  
a2ensite self-service-password  
  
# Add scripts (i.e. entrypoint)  
ADD ["assets/scripts/*", "${SCRIPT_DIR}/"]  
RUN chmod -R u+x ${SCRIPT_DIR}  
  
EXPOSE 80  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["app:start"]  
  


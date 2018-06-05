#  
# Builds a custom docker image for latest Nextcloud Full Apache  
#  
FROM nextcloud:apache  
  
LABEL description="A server software for creating file hosting services" \  
Author="MiGoller"  
  
# setup additional apt repos and update package list  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list \  
&& apt-get update  
  
# CRON related stuff ...  
# install CRON related packages  
RUN apt-get install -y \  
supervisor \  
cron  
  
# setup CRON job for nextcloud  
RUN echo "*/15 * * * * su - www-data -s /bin/bash -c \"php -f
/var/www/html/cron.php\""| crontab -  
  
# set SUPERVISOR settings  
RUN mkdir /var/log/supervisord /var/run/supervisord  
COPY ./config/supervisord/supervisord.conf /etc/supervisor/supervisord.conf  
  
# IMAP related stuff ...  
# install IMAP related packages  
RUN apt-get install -y \  
libc-client-dev \  
libkrb5-dev  
  
# configure and install PHP-extensions for IMAP support  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install imap  
  
# SMB related stuff ...  
# install SMB related packages  
RUN apt-get install -y \  
# libsmbclient-dev \  
smbclient  
  
# PREVIEW related stuff  
# install PREVIEW related packages  
RUN apt-get install -y \  
ffmpeg \  
libmagickwand-dev \  
libgmp3-dev \  
libc-client-dev  
# LibreOffice  
# configure and install PHP-extensions for PREVIEW support  
RUN ln -s "/usr/include/$(dpkg-architecture --query
DEB_BUILD_MULTIARCH)/gmp.h" /usr/include/gmp.h \  
&& docker-php-ext-install bz2 gmp  
  
# RUN pecl install imagick smbclient \  
RUN pecl install imagick \  
# && docker-php-ext-enable imagick smbclient  
&& docker-php-ext-enable imagick  
  
# cleanup apt lists  
RUN rm -rf /var/lib/apt/lists/*  
  
# set recommended PHP.ini settings  
# see
https://docs.nextcloud.com/server/12/admin_manual/configuration_server/server_tuning.html#enable-
php-opcache  
COPY ./config/php/conf.d/apcu.ini /php/conf.d/  
COPY ./config/php/conf.d/opcache.ini /php/conf.d/  
  
CMD ["/usr/bin/supervisord"]  


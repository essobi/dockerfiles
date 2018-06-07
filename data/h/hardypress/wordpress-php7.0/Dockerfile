FROM php:7.0-apache  
MAINTAINER Claudio Benvenuti <claudio@hardypress.com>  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
curl \  
psmisc \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
tcpdump \  
libmcrypt-dev \  
zlib1g-dev \  
openssh-server \  
sendmail \  
mysql-client ; \  
mkdir -p /var/run/sshd; \  
rm -f /etc/ssh/ssh_host_*key*; \  
docker-php-ext-install iconv mcrypt calendar; \  
docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-freetype-dir=/usr/include/freetype2 \  
\--with-png-dir=/usr/include \  
\--with-jpeg-dir=/usr/include; \  
docker-php-ext-install gd mbstring mysqli opcache zip  
  
# TODO consider removing the *-dev deps and only keeping the necessary lib*
packages  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN a2enmod rewrite expires  
  
RUN curl --insecure -o /pagespeed.deb https://dl-
ssl.google.com/dl/linux/direct/mod-pagespeed-stable_current_amd64.deb; \  
dpkg -i /pagespeed.deb; \  
apt-get -f install; \  
rm -rf /var/lib/apt/lists/*; \  
rm /pagespeed.deb  
  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY php.ini /usr/local/etc/php/  
COPY pagespeed.conf /etc/apache2/mods-available  
  
COPY install.sh /root/hardypress/scripts/  
COPY error.html /root/hardypress/scripts/  
COPY wp-cli.phar /root/hardypress/scripts/  
COPY activity_monitor.sh /root/hardypress/scripts/  
COPY hardypress /root/hardypress/plugins/hardypress  
  
COPY ssh /root/ssh_files  
  
EXPOSE 80  
EXPOSE 443  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
COPY sftp_entrypoint.sh /  
RUN chmod +x /sftp_entrypoint.sh  
WORKDIR /root/hardypress/scripts  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  


FROM php:7.0-fpm-alpine  
MAINTAINER Martin Campbell <martin@campbellsoftware.co.uk>  
  
# setup workdir  
RUN mkdir /data  
WORKDIR /data  
  
# environment for osticket  
ENV OSTICKET_VERSION 1.10.1  
ENV HOME /data  
  
# requirements and PHP extensions  
RUN apk add --update \  
wget \  
unzip \  
msmtp \  
ca-certificates \  
supervisor \  
nginx \  
libpng \  
c-client \  
openldap \  
libintl \  
libxml2 \  
icu \  
openssl && \  
apk add imap-dev libpng-dev curl-dev openldap-dev gettext-dev libxml2-dev icu-
dev autoconf g++ make pcre-dev && \  
docker-php-ext-install gd curl ldap mysqli sockets gettext mbstring xml intl
opcache && \  
docker-php-ext-configure imap --with-imap-ssl && \  
docker-php-ext-install imap && \  
pecl install apcu && docker-php-ext-enable apcu && \  
apk del imap-dev libpng-dev curl-dev openldap-dev gettext-dev libxml2-dev icu-
dev autoconf g++ make pcre-dev && \  
rm -rf /var/cache/apk/*  
  
# Download & install OSTicket  
RUN wget -nv -O osTicket.zip
http://osticket.com/sites/default/files/download/osTicket-v${OSTICKET_VERSION}.zip
&& \  
unzip osTicket.zip && \  
rm osTicket.zip && \  
chown -R www-data:www-data /data/upload/ && \  
chmod -R a+rX /data/upload/ /data/scripts/ && \  
chmod -R u+rw /data/upload/ /data/scripts/ && \  
mv /data/upload/setup /data/upload/setup_hidden && \  
chown -R root:root /data/upload/setup_hidden && \  
chmod 700 /data/upload/setup_hidden  
  
# Download languages packs  
RUN wget -nv -O upload/include/i18n/fr.phar
http://osticket.com/sites/default/files/download/lang/fr.phar && \  
wget -nv -O upload/include/i18n/ar.phar
http://osticket.com/sites/default/files/download/lang/ar.phar && \  
wget -nv -O upload/include/i18n/pt_BR.phar
http://osticket.com/sites/default/files/download/lang/pt_BR.phar && \  
wget -nv -O upload/include/i18n/it.phar
http://osticket.com/sites/default/files/download/lang/it.phar && \  
wget -nv -O upload/include/i18n/es_ES.phar
http://osticket.com/sites/default/files/download/lang/es_ES.phar && \  
wget -nv -O upload/include/i18n/de.phar
http://osticket.com/sites/default/files/download/lang/de.phar && \  
mv upload/include/i18n upload/include/i18n.dist  
  
# Download LDAP plugin  
RUN wget -nv -O upload/include/plugins/auth-ldap.phar
http://osticket.com/sites/default/files/download/plugin/auth-ldap.phar  
  
# Configure nginx, PHP, msmtp and supervisor  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY php-osticket.ini $PHP_INI_DIR/conf.d/  
RUN touch /var/log/msmtp.log && \  
chown www-data:www-data /var/log/msmtp.log  
COPY supervisord.conf /data/supervisord.conf  
COPY msmtp.conf /data/msmtp.conf  
COPY php.ini $PHP_INI_DIR/php.ini  
  
COPY bin/ /data/bin  
  
VOLUME
["/data/upload/include/plugins","/data/upload/include/i18n","/var/log/nginx"]  
EXPOSE 80  
CMD ["/data/bin/start.sh"]  


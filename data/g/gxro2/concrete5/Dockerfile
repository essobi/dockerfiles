FROM alpine  
  
RUN set -x && \  
apk add --update \  
bash vim less unzip \  
apache2 \  
curl \  
php7 \  
php7-apache2 \  
php7-json \  
php7-ctype \  
php7-mbstring \  
php7-zip \  
php7-dom \  
php7-xml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-simplexml \  
php7-fileinfo \  
php7-pdo \  
php7-pdo_mysql \  
php7-gd \  
php7-curl \  
php7-iconv \  
php7-tokenizer \  
php7-mcrypt \  
php7-iconv \  
php7-tokenizer \  
php7-openssl \  
php7-dba \  
php7-phpdbg \  
php7-xsl \  
php7-enchant \  
php7-pspell \  
php7-dev \  
php7-pear-mail_mime \  
php7-xmlrpc \  
php7-embed \  
php7-pear-auth_sasl2 \  
php7-exif \  
php7-recode \  
php7-opcache \  
php7-ldap \  
php7-posix \  
php7-pear-net_socket \  
php7-session \  
php7-gettext \  
php7-mailparse \  
php7-sysvshm \  
php7-shmop \  
php7-odbc \  
php7-phar \  
php7-imap \  
php7-pdo_odbc \  
php7-calendar \  
php7-tidy \  
php7-sockets \  
php7-zmq \  
php7-memcached \  
php7-soap \  
php7-apcu \  
php7-sysvmsg \  
php7-zlib \  
php7-imagick-dev \  
php7-ftp \  
php7-sysvsem \  
php7-pear-auth_sasl \  
php7-bz2 \  
php7-mysqli \  
graphviz && \  
sed -i -e '/^#ServerName/aServerName concrete5' /etc/apache2/httpd.conf && \  
sed -i -e 's/\/run\/apache2\/httpd.pid/\/var\/run\/httpd.pid/'
/etc/apache2/conf.d/mpm.conf && \  
sed -i \  
-e '/^;mbstring.language/ambstring.language = neutral' \  
-e '/^;mbstring.http_input/ambstring.http_input = pass' \  
-e '/^;mbstring.encoding_translation/ambstring.encoding_translation = Off' \  
/etc/php7/php.ini && \  
printf '#!/bin/sh\nrm -f /var/run/httpd.pid\nexec httpd -DFOREGROUND' >
/usr/local/bin/httpd-foreground && \  
chmod +x /usr/local/bin/httpd-foreground && \  
echo done.  
  
RUN set -x && \  
curl -o /usr/local/concrete5-8.1.0.zip
http://www.concrete5.org/download_file/-/view/93797/ && \  
echo done.  
  
RUN set -x && \  
cd /var/www/localhost/htdocs && \  
unzip /usr/local/concrete5-8.1.0.zip && \  
mv concrete5-8.1.0 concrete5 && \  
# mv concrete5-8.1.0/* . && \  
echo done.  
  
VOLUME [ \  
/var/www/localhost/htdocs/concrete5/application/config \  
/var/www/localhost/htdocs/concrete5/application/files \  
/var/www/localhost/htdocs/concrete5/packages \  
]  
WORKDIR /var/www/localhost/htdocs  
  
EXPOSE 80  
  
CMD ["httpd-foreground"]  


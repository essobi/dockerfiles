FROM alpine:edge  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
  
ADD composer.json /opt/drupalextension/  
ADD fulcrum-behat /fulcrum-behat  
  
RUN apk update && \  
apk upgrade --no-cache && \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add \--no-cache dbus firefox git icu-libs libvpx openssl php7 php7-ctype
php7-curl php7-dom php7-fpm php7-ftp php7-gd php7-gettext php7-imap php7-json
php7-ldap php7-mbstring php7-mcrypt php7-mysqli php7-opcache php7-openssl
php7-pdo php7-pdo_mysql php7-phar php7-redis php7-simplexml php7-soap
php7-sockets php7-tokenizer php7-xml php7-xmlreader php7-xmlwriter php7-zlib
php7-zip postfix py-pip ttf-dejavu xvfb && \  
pip install --upgrade pip && \  
pip install selenium requests && \  
wget -O - https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin && \  
cd /opt/drupalextension && \  
composer install && \  
ln -s /opt/drupalextension/bin/behat /usr/bin/behat && \  
adduser -h /var/www/html -s /sbin/nologin -D -H -u 1971 php && \  
chown -R postfix /var/spool/postfix && \  
chgrp -R postdrop /var/spool/postfix/public && \  
chgrp -R postdrop /var/spool/postfix/maildrop && \  
chown -R root /var/spool/postfix/pid && \  
chown root /var/spool/postfix && \  
echo smtputf8_enable = no >> /etc/postfix/main.cf  
  
ENTRYPOINT ["/usr/bin/Xvfb"]  
  
CMD [":99", "-ac"]  


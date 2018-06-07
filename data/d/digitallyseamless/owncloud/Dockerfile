FROM mmckeen/opensuse-13-1  
MAINTAINER Cody Mize <cody@digitallyseamless.com>  
  
RUN zypper -n ref && zypper -n up  
  
# add ownCloud repo + PHP extensions repo and install  
RUN zypper ar -f -c
http://download.opensuse.org/repositories/isv:/ownCloud:/community/openSUSE_13.1/isv:ownCloud:community.repo
&& \  
zypper ar -f -c
http://download.opensuse.org/repositories/server:/php:/extensions/openSUSE_13.1/server:php:extensions.repo
&& \  
zypper -n --gpg-auto-import-keys ref  
  
RUN zypper -n in sudo curl less owncloud glibc-locale php5-APC php5-fileinfo
php5-imap php5-openssl && \  
mv /srv/www/htdocs/owncloud /srv/www/ && rmdir /srv/www/htdocs && mv
/srv/www/owncloud /srv/www/htdocs && \  
sed -i -e 's;/htdocs/owncloud;/htdocs;g' /etc/apache2/conf.d/owncloud.conf &&
\  
sed -i 's/;default_charset = "UTF-8"/default_charset = "UTF-8"/g'
/etc/php5/apache2/php.ini  
  
# create copy of config and apps to be stored in new volume  
RUN cd /srv/www/htdocs && cp -rp apps/ .apps && cp -rp config/ .config  
  
# set owncloud permissions  
RUN chown -R wwwrun:www /srv/www/htdocs && \  
chmod ug+rw /srv/www/htdocs /srv/www/htdocs/* /srv/www/htdocs/3rdparty/*
/srv/www/htdocs/.config/.htaccess  
  
# enable apache modules  
RUN a2enmod php5 && \  
a2enmod proxy && \  
a2enmod proxy_connect && \  
a2enmod proxy_http && \  
a2enmod proxy_ftp && \  
a2enmod rewrite  
  
# enable imap extention for php  
RUN echo -e '; comment out next line to disable imap extension in
php\nextension=imap.so' > /etc/php5/conf.d/imap.ini  
  
# add xmpp bosh proxy to owncloud apache conf  
RUN echo -e '\nSSLProxyEngine on\n<Location /http-bind>\n ProxyPass
https://xmpp.digitallyseamless.com/http-bind/\n ProxyPassReverse
https://xmpp.digitallyseamless.com/http-bind/\n</Location>\n' >>
/etc/apache2/conf.d/owncloud.conf  
  
# install the Digitally Seamless root CA  
RUN curl -o /etc/pki/trust/anchors/Digitally_Seamless_Root_CA.crt
https://raw.githubusercontent.com/DigitallySeamless/certs/master/DigitallySeamless_RootCA.crt
&& update-ca-certificates  
  
# create initialize script  
RUN echo -e '#!/bin/sh\nif [ ! -r /srv/www/htdocs/config/config.php ] || [
"$1" = "upgrade" ]; then\n cd /srv/www/htdocs && cp -rp .config/* config/ &&
cp -rp .apps/* apps/\nfi\n[[ "$1" != "upgrade" ]] && /usr/sbin/start_apache2
-D SYSTEMD -D FOREGROUND -k start' > /bin/init && chmod +x /bin/init  
  
# set entrypoint  
ENTRYPOINT ["/bin/init"]  
  
# expose HTTP and HTTPS  
EXPOSE 80 443  
# set environment  
ENV TERM=xterm  


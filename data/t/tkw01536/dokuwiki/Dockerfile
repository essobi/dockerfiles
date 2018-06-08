FROM alpine:3.7  
LABEL maintainer Tom Wiesing <tom@tkw01536.de>  
  
RUN apk add --no-cache \  
bash wget tar gzip curl lighttpd \  
php7-common php7-session php7-zlib php7-openssl php7-iconv php7-json php7-gd
php7-curl php7-xml php7-pgsql php7-imap php7-cgi fcgi php7-pdo php7-pdo_pgsql
php7-soap php7-xmlrpc php7-posix php7-mcrypt php7-gettext php7-ldap php7-ctype
php7-dom  
  
RUN mkdir -p /opt/dokuwiki  
WORKDIR /opt/dokuwiki  
  
# Download dokuwiki  
RUN wget -O dokuwiki.tgz "http://download.dokuwiki.org/src/dokuwiki/dokuwiki-
stable.tgz" \  
&& tar -zxf dokuwiki.tgz --strip-components=1 && rm dokuwiki.tgz \  
&& mkdir /var/run/lighttpd \  
&& chmod -R 755 /opt/dokuwiki /var/log/lighttpd && chmod -R 777 /opt/dokuwiki
&& chown -R lighttpd:lighttpd /opt/dokuwiki /var/log/lighttpd
/var/run/lighttpd \  
&& sed -i -e "s/display_errors = Off/display_errors = On/g" /etc/php7/php.ini  
  
# Configure lighttpd  
ADD lighttpd.conf /etc/lighttpd/lighttpd.conf  
  
EXPOSE 80  
VOLUME /opt/dokuwiki/data  
VOLUME /opt/dokuwiki/lib/plugins  
VOLUME /opt/dokuwiki/conf  
VOLUME /opt/dokuwiki/lib/tpl  
  
ENTRYPOINT ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  


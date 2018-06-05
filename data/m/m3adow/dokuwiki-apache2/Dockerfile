FROM php:5-apache  
MAINTAINER m3adow  
  
RUN curl http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz | tar
xzvf - --strip 1 \  
&& chown -R www-data:www-data /var/www/html/* /var/www/html/.[!.]*
/var/www/html/.??* \  
# Add ServerName direvtive if VIRTUAL_HOST is set  
&& sed -i -e '/^exec/ i VIRTUAL_HOST=${VIRTUAL_HOST:-} \  
[ -n "${VIRTUAL_HOST}" ] && echo "ServerName ${VIRTUAL_HOST}" >
/etc/apache2/conf-enabled/ServerName.conf \  
' /usr/local/bin/apache2-foreground  
COPY ["./wannabe-user.sh/wannabe-user.sh", "/usr/local/bin/"]  
VOLUME ["/var/www/html/data/pages/", "/var/www/html/data/meta/",
"/var/www/html/data/media/", \  
"/var/www/html/data/media_meta/", "/var/www/html/data/attic/", \  
"/var/www/html/data/media_attic/", "/var/www/html/conf/",
"/var/www/html/lib/plugins"]  
  
EXPOSE 80 443  
ENTRYPOINT ["/usr/local/bin/wannabe-user.sh", "-u", "33", "-g", "33", "-f",
"/var/www/html/conf"]  
CMD ["/usr/local/bin/apache2-foreground"]  


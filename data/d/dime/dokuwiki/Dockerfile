FROM dime/php-fpm  
  
ARG DOKUWIKI_VERSION=2017-02-19e  
ARG DOKUWIKI_CSUM=09bf175f28d6e7ff2c2e3be60be8c65f  
  
RUN wget -q -O /dokuwiki.tgz
"http://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" &&
\  
if [ "$DOKUWIKI_CSUM" != "$(md5sum /dokuwiki.tgz | awk '{print($1)}')" ];then
echo "Wrong md5sum of downloaded file!"; exit 1; fi && \  
mkdir /var/www/dokuwiki && \  
tar -zxf /dokuwiki.tgz -C /var/www/dokuwiki --strip-components 1 && \  
rm /dokuwiki.tgz  
  
RUN chown -R www-data:www-data /var/www/dokuwiki  
  
VOLUME ["/var/www/dokuwiki"]


FROM alpine:3.6  
MAINTAINER engineering@finbourne.com  
  
ENV DOKUWIKI_VERSION c5525093cf2c4f47e2e5d2439fe13964  
EXPOSE 80  
  
RUN apk --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ add \  
php7 php7-fpm php7-gd php7-session php7-xml nginx supervisor curl tar zip  
  
RUN mkdir -p /run/nginx && \  
mkdir -p /var/www /var/dokuwiki-storage/data && \  
cd /var/www && \  
curl -O -L "https://download.dokuwiki.org/out/dokuwiki-$DOKUWIKI_VERSION.tgz"
&& \  
tar -xzf "dokuwiki-$DOKUWIKI_VERSION.tgz" \--strip 1 && \  
rm "dokuwiki-$DOKUWIKI_VERSION.tgz" && \  
curl --output template.zip -L
"https://github.com/evnix/codowik/archive/master.zip" && \  
unzip template.zip -d /var/www/lib/tpl/ && \  
mv /var/www/lib/tpl/codowik-master /var/www/lib/tpl/codowik && \  
cd /var/www/lib/plugins && \  
curl -O -L "https://github.com/cosmocode/edittable/archive/2017-06-07.tar.gz"
&& \  
tar -xzf 2017-06-07.tar.gz && \  
rm 2017-06-07.tar.gz && \  
mv edittable-2017-06-07 edittable && \  
curl -O -L "https://github.com/Chris--S/dokuwiki-plugin-
iframe/archive/master.zip" && \  
unzip master.zip && \  
mv dokuwiki-plugin-iframe-master/ iframe && \  
rm master.zip && \  
curl -O -L "https://komkon2.de/markdowku/markdowku.tgz" && \  
tar -xzf markdowku.tgz && \  
rm markdowku.tgz && \  
curl --output color.zip -L
"https://github.com/leeyc0/dokuwiki_plugin_color/zipball/master" && \  
unzip color.zip -d /var/www/lib/plugins/ && \  
mv /var/www/lib/plugins/leeyc0-dokuwiki_plugin_color-b0613b8/ color && \  
mv /var/www/data/pages /var/dokuwiki-storage/data/pages && \  
ln -s /var/dokuwiki-storage/data/pages /var/www/data/pages && \  
mv /var/www/data/meta /var/dokuwiki-storage/data/meta && \  
ln -s /var/dokuwiki-storage/data/meta /var/www/data/meta && \  
mv /var/www/data/media /var/dokuwiki-storage/data/media && \  
ln -s /var/dokuwiki-storage/data/media /var/www/data/media && \  
mv /var/www/data/media_attic /var/dokuwiki-storage/data/media_attic && \  
ln -s /var/dokuwiki-storage/data/media_attic /var/www/data/media_attic && \  
mv /var/www/data/media_meta /var/dokuwiki-storage/data/media_meta && \  
ln -s /var/dokuwiki-storage/data/media_meta /var/www/data/media_meta && \  
mv /var/www/data/attic /var/dokuwiki-storage/data/attic && \  
ln -s /var/dokuwiki-storage/data/attic /var/www/data/attic && \  
mv /var/www/conf /var/dokuwiki-storage/conf && \  
ln -s /var/dokuwiki-storage/conf /var/www/conf  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisord.conf  
ADD start.sh /start.sh  
  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php7/php-fpm.ini && \  
sed -i -e "s|;daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf &&
\  
sed -i -e "s|listen\s*=\s*127\\.0\\.0\\.1:9000|listen = /var/run/php-
fpm7.sock|g" /etc/php7/php-fpm.d/www.conf && \  
sed -i -e "s|;listen\\.owner\s*=\s*|listen.owner = |g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s|;listen\\.group\s*=\s*|listen.group = |g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s|;listen\\.mode\s*=\s*|listen.mode = |g" /etc/php7/php-
fpm.d/www.conf && \  
chmod +x /start.sh && \  
chown -R nobody:root /var/www/* && \  
chown -R nobody:root /var/tmp/nginx/ && \  
chown -R nobody:root /var/www/.*  
  
VOLUME ["/var/dokuwiki-storage"]  
  
CMD /start.sh  


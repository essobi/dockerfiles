FROM reangd/alpine-nginx:latest  
  
RUN DOKUWIKI_VERSION="2017-02-19e" && \  
apk add --no-cache \  
php7-openssl php7-fpm php7-json php7-gd \  
php7-session php7-zip php7-zlib php7-cgi \  
php7-sqlite3 php7-xml php7-pdo_sqlite && \  
\  
sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php7/php.ini && \  
curl -sSL
http://download.dokuwiki.org/src/dokuwiki/dokuwiki-${DOKUWIKI_VERSION}.tgz |
tar xz -C /tmp && \  
mkdir /www && \  
mv /tmp/dokuwiki-${DOKUWIKI_VERSION}/ /www/dokuwiki && \  
chown -R nobody:www-data /www/ && \  
chmod -R 644 /www/ && \  
find /www/ -type d -exec chmod 0755 {} ';' && \  
\  
mkdir -p /origin/lib && \  
cp -rp /www/dokuwiki/data /origin/ && \  
cp -rp /www/dokuwiki/conf /origin/ && \  
cp -rp /www/dokuwiki/lib/plugins /origin/lib/ && \  
cp -rp /www/dokuwiki/lib/tpl /origin/lib/ && \  
\  
rm -rf /www/dokuwiki/data /www/dokuwiki/conf /www/dokuwiki/lib/plugins
/www/dokuwiki/lib/tpl && \  
ln -s /data/data /www/dokuwiki/data && \  
ln -s /data/conf /www/dokuwiki/conf && \  
ln -s /data/lib/plugins /www/dokuwiki/lib/plugins && \  
ln -s /data/lib/tpl /www/dokuwiki/lib/tpl  
  
COPY root /  


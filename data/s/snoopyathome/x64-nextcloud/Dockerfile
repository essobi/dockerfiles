FROM alpine:3.7  
  
RUN apk add \--update ca-certificates openssl nginx nginx-mod-http-headers-
more tar gzip wget bzip2 &&\  
apk add \--update-cache --repository
http://dl-3.alpinelinux.org/alpine/v3.7/community/ php7 php7-gettext php7-fpm
php7-ctype php7-dom php7-gd php7-iconv php7-json php7-xml php7-xmlreader
php7-posix php7-zlib php7-zip php7-curl php7-opcache php7-openssl php7-mcrypt
php7-apcu php7-ldap php7-intl php7-pdo_pgsql php7-pgsql &&\  
mkdir -p /tmp/nginx/client-body  
  
COPY files/etc/php /etc/php5  
COPY files/start.sh /start.sh  
  
RUN wget
https://download.nextcloud.com/server/releases/nextcloud-13.0.2.tar.bz2 &&\  
bunzip2 nextcloud-13.0.2.tar.bz2 &&\  
tar xf nextcloud-13.0.2.tar &&\  
rm nextcloud-13.0.2.tar &&\  
mv nextcloud web &&\  
chown -R nginx:www-data /web &&\  
chown -R nginx /var/lib/nginx &&\  
chmod +x /start.sh &&\  
apk del wget bzip2 tar &&\  
rm -rf /var/cache/apk/*  
  
CMD ["/start.sh"]  


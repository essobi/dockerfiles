#  
# Dockerfile for dokuwiki  
#  
  
FROM alpine  
MAINTAINER Andreas Peters <noreply@aventer.biz>  
  
ENV BACKUP_PATH = '/s3backup'  
  
WORKDIR /var/www/html  
  
RUN set -xe \  
&& apk add --no-cache ca-certificates \  
gzip \  
nginx \  
openssl \  
php5-fpm \  
php5-openssl \  
php5-pdo_sqlite \  
php5-sqlite3 \  
php5-xml \  
php5-zlib \  
python \  
tar \  
&& touch /etc/php5/fpm.d/empty.conf \  
&& wget -O- http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz |
tar xz --strip 1 \  
&& chown -R nobody:nobody .  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY backup.py /usr/local/bin/backup.py  
  
RUN chown -R nobody:nobody /var/www/html/lib \  
&& chmod +x /usr/local/bin/backup.py \  
&& ln -s /usr/local/bin/backup.py /etc/periodic/15min/backup.py  
  
VOLUME ["/var/www/html/conf"]  
  
RUN chmod 775 /var/www/html/conf  
  
EXPOSE 8888  
  
CMD crond && php-fpm5 && nginx -g 'daemon off;'  


FROM castorinop/php-nextcloud  
  
#https://updates.nextcloud.com/server/  
# FIXME: get latest version  
# curl -L
https://updates.nextcloud.org/updater_server/?version=9x0x0x12x1448709225.0768x1448709281xstablexx2015-10-19T18:44:30+00:00%208ee2009de36e01a9866404f07722892f84c16e3e
-A 'Nextcloud Updater' |sed 's@<version>\\(.*\\)</version>@\1@g'  
ENV VERSION 12.0.5  
ENV URLBASE http://download.nextcloud.com/server/releases  
  
RUN mkdir /app  
WORKDIR /app  
  
RUN apk add curl --update --no-cache  
  
#FIXME: use https://download.nextcloud.com/download/community/setup-
nextcloud.php  
RUN curl -Lk $URLBASE/nextcloud-${VERSION}.tar.bz2 >
nextcloud-${VERSION}.tar.bz2 && \  
curl -Lk $URLBASE/nextcloud-${VERSION}.tar.bz2.md5 >
nextcloud-${VERSION}.tar.bz2.md5 && \  
md5sum nextcloud-${VERSION}.tar.bz2 && tar jxf nextcloud-${VERSION}.tar.bz2 &&
\  
rm nextcloud-${VERSION}.tar.bz2  
  
COPY noarch/occ.sh /usr/local/bin/occ  
RUN chmod +x /app/nextcloud/occ /usr/local/bin/occ  
  
VOLUME ["/data"]  
VOLUME ["/app/nextcloud/config"]  
VOLUME ["/app/nextcloud"]  
  
COPY run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
RUN apk add --update sudo  
  
ENTRYPOINT ["/usr/local/bin/run"]  
  
WORKDIR /app/nextcloud  
  
COPY config/nginx.conf /etc/nginx/conf.d/nextcloud.conf  
VOLUME ["/etc/nginx/conf.d"]  
  
COPY config/nextcloud.ini /etc/php7/conf.d/nextcloud.ini  
COPY config/opcache.ini /etc/php7/conf.d/opcache.ini  
COPY config/apcu.ini /etc/php7/conf.d/apcu.ini  
VOLUME ["/etc/php7/conf.d"]  


FROM alpine:edge  
  
LABEL maintainer "Peerasan Buranasanti <peerasan@gmail.com>"  
  
# Stable Repo  
#RUN apk upgrade -U && apk --update
--repository=http://dl-4.alpinelinux.org/alpine/edge/testing
--repository=http://dl-4.alpinelinux.org/alpine/edge/main add \  
RUN apk upgrade -U && apk --no-cache add \  
supervisor tzdata nginx ffmpeg imagemagick \  
php7 php7-fpm php7-fileinfo php7-tokenizer php7-json php7-session
php7-mbstring php7-mysqli php7-pdo_mysql php7-mysqlnd php7-openssl php7-mcrypt
php7-xml php7-curl php7-ctype \  
php7-gd php7-imagick php7-exif php7-phar php7-dom php7-zlib php7-memcached &&
\  
cp -r /etc/php7 /etc/php7.orig && \  
cp -r /etc/nginx /etc/nginx.orig && \  
cp -r /etc/supervisord.conf /etc/supervisord.conf.orig  
  
COPY fs /  
  
# ensure www-data user exists  
# 82 is the standard uid/gid for "www-data" in Alpine  
RUN set -x ; \  
addgroup -g 82 -S www-data ; \  
adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1 \  
mkdir -p /apps; chown -Rf www-data:www-data /apps  
  
#CLEAN  
RUN mkdir -p /apps; \  
mkdir -p /var/run/php; \  
mkdir -p /var/log/php7; \  
chown -Rf nginx:nginx /apps  
  
RUN rm /var/cache/apk/*;  
  
EXPOSE 80  
ADD run.sh /root/run.sh  
CMD /bin/sh /root/run.sh  


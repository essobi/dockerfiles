FROM alpine:3.6  
  
MAINTAINER MAB <docker@mab.net>  
  
RUN apk add \--update \  
rtorrent \  
nginx \  
php7 \  
php7-fpm \  
php7-json \  
curl \  
gzip \  
zip \  
unrar \  
supervisor \  
git \  
geoip \  
ffmpeg  
  
RUN curl https://codeload.github.com/Novik/ruTorrent/tar.gz/v3.8 \  
| tar -zxv -C / \  
&& mv /ruTorrent-3.8 /rutorrent  
  
RUN mkdir -p /tmp/nginx/client-body /downloads/incoming /downloads/completed
/downloads/watched /downloads/sessions /tmp/rtorrent \  
&& adduser -D -h / -u 500 rtorrent \  
&& chown -R rtorrent:rtorrent /downloads /rutorrent /tmp/rtorrent
/var/lib/nginx /var/tmp/nginx\  
&& sed -i \  
-e 's/group =.*/group = rtorrent/' \  
-e 's/user =.*/user = rtorrent/' \  
-e 's/listen\.owner.*/listen\.owner = rtorrent/' \  
-e 's/listen\.group.*/listen\.group = rtorrent/' \  
-e 's/error_log =.*/error_log = \/dev\/stdout/' \  
/etc/php7/php-fpm.d/www.conf \  
&& sed -i \  
-e '/open_basedir =/s/^/\;/' \  
/etc/php7/php.ini \  
&& sed -i \  
-e "/curl/ s/''/'\/usr\/bin\/curl'/" \  
-e "/php/ s/''/'\/usr\/bin\/php7'/" \  
/rutorrent/conf/config.php \  
&& rm -rf /var/cache/apk/*  
  
ARG plugins=  
  
RUN curl \--silent \--show-error \--fail \--location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/amd64?plugins=${plugins}" \  
| tar \--no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
COPY supervisord-rtorrent.ini /etc/supervisor.d/supervisord-rtorrent.ini  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
COPY Caddyfile /etc/Caddyfile  
  
COPY auth_file /etc/nginx/auth_file  
  
COPY rtorrent.conf /.rtorrent.rc  
  
VOLUME /downloads  
  
EXPOSE 80 5000 6881 51413  
  
CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  


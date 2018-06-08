FROM mitcdh/caddy-php  
MAINTAINER Mitchell Hewes <me@mitcdh.com>  
  
RUN apk --update add \  
php7-pdo_pgsql \  
php7-pdo_mysql && \  
rm -rf /var/cache/apk/*  
  
COPY files/miniflux-vol.sh /caddy-bootstrap/pre-run/01_miniflux-vol  
COPY files/miniflux-config.sh /caddy-bootstrap/pre-run/02_miniflux-config  
COPY files/miniflux-cron.sh /caddy-bootstrap/pre-run/03_miniflux-cron  
  
COPY files/Caddyfile /caddy-bootstrap/Caddyfile  
COPY files/miniflux-install.sh /www/miniflux-install.sh  
  
RUN chmod 500 /caddy-bootstrap/pre-run/* \  
&& install -o www-data -g www-data -d /www/public \  
&& install -o www-data -g www-data -d /www/public/data  
  
VOLUME /www/public/data  
  
EXPOSE 2015  


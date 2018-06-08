FROM alpine:latest  
  
MAINTAINER Peter Szalatnay <theotherland@gmail.com>  
  
RUN \  
addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& apk add --no-cache \  
curl \  
&& mkdir -p /usr/share/nginx/html \  
&& curl -o rainloop.zip -SL
http://repository.rainloop.net/v2/webmail/rainloop-latest.zip \  
&& unzip rainloop.zip -d /usr/share/nginx/html \  
&& rm rainloop.zip \  
&& chown -Rf nginx.nginx /usr/share/nginx/html  
  
COPY ./default.conf /etc/nginx/conf.d/  
  
VOLUME ["/usr/share/nginx/html", "/etc/nginx/conf.d/"]


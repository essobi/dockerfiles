FROM alpine:latest  
  
MAINTAINER Felix Buenemann <felix.buenemann@gmail.com>  
  
ENV NGINX_VERSION 1.9.12  
ENV NGINX_AUTH_LDAP_VERSION 8517bb05ecc896b54429ca5e95137b0a386bd41a  
  
ENV GPG_KEYS B0F4253373F8F6F510D42178520A9993A1C052F8  
ENV CONFIG "\  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--http-client-body-temp-path=/var/cache/nginx/client_temp \  
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
--user=nginx \  
--group=nginx \  
--with-http_ssl_module \  
--with-http_realip_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_stub_status_module \  
--with-file-aio \  
--with-http_v2_module \  
--with-ipv6 \  
"  
  
ENV CFLAGS "-O2 -pipe -fomit-frame-pointer -march=core2 -mtune=intel"  
  
RUN \  
addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
openldap-dev \  
linux-headers \  
curl \  
gnupg \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& gpg --verify nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz* \  
&& rm -r /root/.gnupg \  
&& curl -fSL https://github.com/kvspb/nginx-auth-
ldap/archive/$NGINX_AUTH_LDAP_VERSION.tar.gz -o nginx-auth-
ldap-$NGINX_AUTH_LDAP_VERSION.tar.gz \  
&& tar -zxC /usr/src -f nginx-auth-ldap-$NGINX_AUTH_LDAP_VERSION.tar.gz \  
&& rm nginx-auth-ldap-$NGINX_AUTH_LDAP_VERSION.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG --add-module=/usr/src/nginx-auth-
ldap-$NGINX_AUTH_LDAP_VERSION \  
&& make install \  
&& strip /usr/sbin/nginx \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/src/nginx-* \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  


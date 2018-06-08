FROM alpine:latest  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
  
ENV NGINX_VERSION 1.13.4  
  
ENV GPG_KEYS B0F4253373F8F6F510D42178520A9993A1C052F8  
ENV CONFIG "\  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--modules-path=/usr/lib/nginx/modules \  
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
--with-http_addition_module \  
--with-http_sub_module \  
--with-http_dav_module \  
--with-http_flv_module \  
--with-http_mp4_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_stub_status_module \  
--with-http_auth_request_module \  
--with-http_xslt_module=dynamic \  
--with-http_image_filter_module=dynamic \  
--with-http_geoip_module=dynamic \  
--with-http_perl_module=dynamic \  
--with-threads \  
--with-stream \  
--with-stream_ssl_module \  
--with-stream_ssl_preread_module \  
--with-stream_realip_module \  
--with-stream_geoip_module=dynamic \  
--with-http_slice_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-compat \  
--with-file-aio \  
--with-http_v2_module \  
"  
  
ENV CFLAGS "-O2 -pipe -fomit-frame-pointer -march=core2 -mtune=intel"  
  
RUN \  
addgroup -g 1971 -S nginx && \  
adduser -D -S -u 1971 -h /var/cache/nginx -s /sbin/nologin -G nginx nginx && \  
apk add --no-cache freetype gd geoip libgcrypt libgpg-error libintl libjpeg-
turbo libpng libxml2 libxslt && \  
apk add --no-cache --virtual .build-deps \  
gcc make linux-headers curl gnupg perl mercurial \  
gd-dev geoip-dev libxslt-dev libc-dev openssl-dev pcre-dev perl-dev zlib-dev
&& \  
gpg --keyserver pool.sks-keyservers.net --recv-keys "$GPG_KEYS" && \  
curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz && \  
curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc && \  
gpg --verify nginx.tar.gz.asc && \  
mkdir -p /usr/src && \  
tar -zxC /usr/src -f nginx.tar.gz && \  
rm nginx.tar.gz* && \  
rm -r /root/.gnupg && \  
hg clone http://hg.nginx.org/njs /usr/src/njs && \  
cd /usr/src/nginx-$NGINX_VERSION && \  
./configure $CONFIG --add-module=/usr/src/njs/nginx && \  
make install && \  
strip /usr/sbin/nginx && \  
runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" && \  
apk add --virtual .nginx-rundeps $runDeps && \  
apk del .build-deps && \  
rm -rf /usr/src/*  
  
EXPOSE 80 443  
  
  
ENTRYPOINT ["/usr/sbin/nginx"]  
#CMD ["nginx", "-g", "daemon off;"]  


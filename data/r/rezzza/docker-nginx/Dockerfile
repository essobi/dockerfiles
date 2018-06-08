FROM alpine:latest  
  
MAINTAINER Sébastien HOUZÉ <sebastien.houze@verylastroom.com>  
  
ENV VERSION=1.9.12 \  
GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
DEVEL_KIT_VERSION=0.2.19 \  
LUA_MODULE_VERSION=0.10.2  
  
ENV CONFIGURE_OPTIONS "\  
--prefix=/etc/nginx \  
--add-module=/usr/src/ngx_devel_kit-$DEVEL_KIT_VERSION \  
--add-module=/usr/src/lua-nginx-module-$LUA_MODULE_VERSION \  
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
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_stub_status_module \  
--with-http_auth_request_module \  
--with-threads \  
--with-stream \  
--with-stream_ssl_module \  
--with-http_slice_module \  
--with-file-aio \  
--with-http_v2_module \  
--with-ipv6 \  
"  
  
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
linux-headers \  
curl \  
gnupg \  
luajit-dev \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
&& curl -fSL http://nginx.org/download/nginx-$VERSION.tar.gz -o nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& gpg --verify nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz* \  
&& rm -r /root/.gnupg \  
&& curl -fSL
https://github.com/simpl/ngx_devel_kit/archive/v$DEVEL_KIT_VERSION.tar.gz -o
ngx_devel_kit-$DEVEL_KIT_VERSION.tar.gz \  
&& tar -zxC /usr/src -f ngx_devel_kit-$DEVEL_KIT_VERSION.tar.gz \  
&& rm ngx_devel_kit-$DEVEL_KIT_VERSION.tar.gz \  
&& curl -fSL https://github.com/openresty/lua-nginx-
module/archive/v$LUA_MODULE_VERSION.tar.gz -o lua-nginx-module.tar.gz \  
&& tar -zxC /usr/src -f lua-nginx-module.tar.gz \  
&& rm lua-nginx-module.tar.gz \  
&& cd /usr/src/nginx-$VERSION \  
&& ./configure $CONFIGURE_OPTIONS --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& ./configure $CONFIGURE_OPTIONS \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so || true \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/src/nginx-* \  
&& rm -rf /usr/src/ngx_devel_kit-* \  
&& rm -rf /usr/src/lua-nginx-module-* \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  


FROM alpine:3.7  
LABEL maintainer="NGINX Docker Maintainers <gd.shunhua@qq.com>"  
  
ENV NGINX_VERSION 1.13.9  
ENV LUAJIT_VERSION 2.1.0-beta3  
ENV LUAJIT_LIB /usr/local/lib  
ENV LUAJIT_INC /usr/local/include/luajit-2.1  
ENV OPESNSSL 1.0.2o  
  
RUN set -x \  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
zlib-dev \  
pcre-dev \  
gd-dev \  
geoip-dev \  
libxslt-dev \  
make \  
linux-headers \  
wget \  
curl \  
gnupg \  
perl-dev \  
unzip \  
&& apk add --no-cache pcre zlib gd geoip libxslt libgcc perl \  
&& wget -O openssl.tar.gz
https://www.openssl.org/source/openssl-$OPESNSSL.tar.gz \  
&& wget -O nginx.tar.gz http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz
\  
&& wget -O ngx_devel_kit.tar.gz
https://codeload.github.com/simplresty/ngx_devel_kit/tar.gz/v0.3.1rc1 --no-
check-certificate \  
&& wget -O lua-nginx-module.tar.gz https://codeload.github.com/openresty/lua-
nginx-module/tar.gz/v0.10.12rc2 --no-check-certificate \  
&& wget -O LuaJIT.tar.gz
http://luajit.org/download/LuaJIT-$LUAJIT_VERSION.tar.gz \  
&& mkdir -p /usr/src/nginx /usr/local/lua-nginx-module
/usr/local/ngx_devel_kit /usr/src/luaJIT \  
&& tar -xzf nginx.tar.gz -C /usr/src/nginx --strip-components=1 \  
&& tar -xzf lua-nginx-module.tar.gz -C /usr/local/lua-nginx-module --strip-
components=1 \  
&& tar -xzf ngx_devel_kit.tar.gz -C /usr/local/ngx_devel_kit --strip-
components=1 \  
&& tar -xzf LuaJIT.tar.gz -C /usr/src/luaJIT --strip-components=1 \  
&& mkdir -p /usr/local/openssl && tar -xzf openssl.tar.gz -C
/usr/local/openssl --strip-components=1 \  
&& rm -f nginx.tar.gz lua-nginx-module.tar.gz ngx_devel_kit.tar.gz
LuaJIT.tar.gz openssl.tar.gz\  
&& cd /usr/src/luaJIT \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& cd /usr/src/nginx \  
&& ./configure --prefix=/usr/local/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--with-http_ssl_module \  
\--with-openssl=/usr/local/openssl \  
\--with-http_perl_module \  
\--with-http_realip_module \  
\--with-http_gzip_static_module \  
\--pid-path=/var/run/nginx.pid \  
\--with-http_geoip_module \  
\--http-fastcgi-temp-path=/var/tmp/nginx/fcgi \  
\--http-scgi-temp-path=/var/tmp/nginx/scgi \  
\--with-ld-opt="-Wl,-rpath,$LUAJIT_LIB" \  
\--add-module=/usr/local/ngx_devel_kit \  
\--add-module=/usr/local/lua-nginx-module \  
\--error-log-path=/usr/local/nginx/logs/error.log \  
\--http-log-path=/usr/local/nginx/logs/access.log \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& make clean \  
&& rm -rf $LUAJIT_LIB/libluajit-5.1.a $LUAJIT_INC \  
&& strip -s /usr/sbin/nginx \  
&& apk --no-cache del .build-deps \  
&& rm -rf /usr/local/lua-nginx-module /usr/local/ngx_devel_kit /usr/src/luaJIT
/usr/src/nginx /usr/local/openssl \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& ln -sf /dev/stdout /usr/local/nginx/logs/access.log \  
&& ln -sf /dev/stderr /usr/local/nginx/logs/error.log \  
&& sed -i '/mime.types/a\include /etc/nginx/conf.d/*.conf;'
/etc/nginx/nginx.conf  
  
EXPOSE 80 443  
STOPSIGNAL SIGTERM  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]


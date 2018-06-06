FROM debian:jessie  
  
MAINTAINER JohnWu "v.la@live.cn"  
  
#runtime dependencies  
RUN \  
apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 1ABFE185 \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
libpcre++0 zlib1g  
  
ENV NGINX_VERSION 1.10.1  
ENV LUA_MODULE_VERSION 0.10.1  
ENV OPENSSL_VERSION 1.0.2h  
ENV LUAJIT_VERSION 2.0.4  
  
ENV CONFIG "\  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--user=nginx \  
\--group=nginx \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_stub_status_module \  
\--with-http_auth_request_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-file-aio \  
\--with-ipv6 \  
\--with-http_v2_module \  
\--with-openssl=/usr/src/openssl-$OPENSSL_VERSION \  
\--add-module=/usr/src/ngx_devel_kit-0.3.0 \  
\--add-module=/usr/src/nginx_upstream_check_module-master \  
\--add-module=/usr/src/lua-nginx-module-$LUA_MODULE_VERSION \  
\--add-module=/usr/src/ngx_cache_purge-2.3 \  
"  
  
RUN set -x \  
&& buildDeps=" \  
ca-certificates \  
gcc \  
libpcre++-dev \  
make \  
curl \  
patch \  
unzip \  
zlib1g-dev \  
" \  
&& apt-get install --no-install-recommends --no-install-suggests -y $buildDeps
\  
&& mkdir -p /tmp && cd /tmp \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx-$NGINX_VERSION.tar.gz \  
&& curl -fSL https://github.com/simpl/ngx_devel_kit/archive/v0.3.0.tar.gz -o
ngx_devel_kit-0.3.0.tar.gz \  
&& curl -fSL https://github.com/openresty/lua-nginx-
module/archive/v$LUA_MODULE_VERSION.tar.gz -o lua-nginx-
module-$LUA_MODULE_VERSION.tar.gz \  
&& curl -fSL https://github.com/FRiCKLE/ngx_cache_purge/archive/2.3.tar.gz -o
ngx_cache_purge-2.3.tar.gz \  
&& curl -fSL
https://github.com/yaoweibin/nginx_upstream_check_module/archive/master.zip -o
nginx_upstream_check_module.zip \  
&& curl -fSL http://luajit.org/download/LuaJIT-$LUAJIT_VERSION.tar.gz -o
LuaJIT-$LUAJIT_VERSION.tar.gz \  
&& curl -fSL https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz -o
openssl-$OPENSSL_VERSION.tar.gz \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx-$NGINX_VERSION.tar.gz \  
&& tar -zxC /usr/src -f ngx_devel_kit-0.3.0.tar.gz \  
&& tar -zxC /usr/src -f lua-nginx-module-$LUA_MODULE_VERSION.tar.gz \  
&& tar -zxC /usr/src -f ngx_cache_purge-2.3.tar.gz \  
&& unzip -ox nginx_upstream_check_module.zip -d /usr/src \  
&& tar -zxC /usr/src -f LuaJIT-$LUAJIT_VERSION.tar.gz \  
&& tar -zxC /usr/src -f openssl-$OPENSSL_VERSION.tar.gz \  
&& addgroup \--system nginx \  
&& adduser \--system --disabled-password --disabled-login --home
/var/www/nginx -uid 1000 \--shell /sbin/nologin nginx \  
&& mkdir -p /var/www/nginx && chown nginx:nginx -R /var/www/nginx \  
&& usermod -aG nginx nginx \  
&& cd /usr/src/LuaJIT-$LUAJIT_VERSION \  
&& make && make install \  
&& export LUAJIT_LIB=/usr/local/lib \  
&& export LUAJIT_INC=/usr/local/include/luajit-2.0 \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& patch -p0 < /usr/src/nginx_upstream_check_module-master/check_1.9.2+.patch
\  
&& mkdir -p /var/log/nginx && mkdir -p /var/cache/nginx \  
&& ./configure $CONFIG \  
&& make && make install \  
&& ldconfig \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir -p /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& strip /usr/sbin/nginx* \  
&& cd / \  
&& apt-get purge --auto-remove -y $buildDeps \  
&& rm -rf /usr/src/* \  
&& rm -rf /tmp* \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY test.conf /etc/nginx/test.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
CMD ["nginx", "-g", "daemon off;"]


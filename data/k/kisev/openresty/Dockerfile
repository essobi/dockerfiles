FROM alpine:3.6  
  
ARG OPENRESTY_VERSION=1.11.2.5  
ARG LUAROCKS_VERSION=2.4.2  
ARG LUA_AUTO_SSL_VERSION=0.11.0  
ARG OPENRESTY_PREFIX=/opt/openresty  
ARG NGINX_PREFIX=/opt/openresty/nginx  
ARG VAR_PREFIX=/var/nginx  
  
RUN echo "--- Install build dependencies ---" \  
&& apk add \--no-cache \--update \--virtual build-deps \  
make \  
gcc \  
musl-dev \  
pcre-dev \  
openssl-dev \  
zlib-dev \  
ncurses-dev \  
readline-dev \  
perl \  
&& echo "--- Install runtime dependencies ---" \  
&& apk add \--no-cache \  
bash \  
curl \  
libpcrecpp \  
libpcre16 \  
libpcre32 \  
openssl \  
libssl1.0 \  
pcre \  
libgcc \  
libstdc++ \  
&& readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& mkdir -p /root/ngx_openresty \  
&& cd /root/ngx_openresty \  
&& echo "--- Download OpenResty ---" \  
&& curl -L http://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz
| tar -xz \  
&& cd openresty-* \  
&& echo "--- Configure OpenResty ---" \  
&& ./configure \  
\--prefix=${OPENRESTY_PREFIX} \  
\--http-client-body-temp-path=${VAR_PREFIX}/client_body_temp \  
\--http-proxy-temp-path=${VAR_PREFIX}/proxy_temp \  
\--http-log-path=${VAR_PREFIX}/access.log \  
\--error-log-path=${VAR_PREFIX}/error.log \  
\--pid-path=${VAR_PREFIX}/nginx.pid \  
\--lock-path=${VAR_PREFIX}/nginx.lock \  
\--with-http_gzip_static_module \  
\--with-http_ssl_module \  
\--with-http_v2_module \  
\--with-luajit \  
\--with-pcre-jit \  
\--with-ipv6 \  
-j${NPROC} \  
&& echo "--- Build OpenResty ---" \  
&& make -j${NPROC} \  
&& echo "--- Install OpenResty ---" \  
&& make install \  
&& ln -sf ${NGINX_PREFIX}/sbin/nginx /usr/local/bin/nginx \  
&& ln -sf ${NGINX_PREFIX}/sbin/nginx /usr/local/bin/openresty \  
&& ln -sf ${OPENRESTY_PREFIX}/bin/resty /usr/local/bin/resty \  
&& ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luajit-*
${OPENRESTY_PREFIX}/luajit/bin/lua \  
&& ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luajit-* /usr/local/bin/lua \  
&& echo "--- Download LuaRocks ---" \  
&& curl -L
http://luarocks.github.io/luarocks/releases/luarocks-${LUAROCKS_VERSION}.tar.gz
| tar -xz \  
&& cd luarocks-* \  
&& echo "--- Configure LuaRocks ---" \  
&& ./configure \  
\--prefix=${OPENRESTY_PREFIX}/luajit \  
\--with-lua=${OPENRESTY_PREFIX}/luajit \  
\--with-lua-include=${OPENRESTY_PREFIX}/luajit/include/luajit-2.1 \  
\--lua-suffix=jit-2.1.0-beta3 \  
&& echo "--- Build LuaRocks ---" \  
&& make -j${NPROC} \  
&& echo "--- Install LuaRocks ---" \  
&& make install \  
&& ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luarocks /usr/local/bin/luarocks \  
&& echo "--- Install lua-resty-auto-ssl module ---" \  
&& luarocks install lua-resty-auto-ssl ${LUA_AUTO_SSL_VERSION} \  
&& echo "--- Configure lua-resty-auto-ssl ---" \  
&& mkdir -p /etc/resty-auto-ssl \  
&& openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 \  
-subj '/CN=sni-support-required-for-valid-ssl' \  
-keyout /etc/ssl/resty-auto-ssl-fallback.key \  
-out /etc/ssl/resty-auto-ssl-fallback.crt \  
&& echo "--- Add group and user for OpenResty ---" \  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& echo "--- Remove build dependencies ---" \  
&& apk del build-deps \  
&& echo "--- Cleanup ---" \  
&& rm -rf /root/ngx_openresty  
  
WORKDIR ${NGINX_PREFIX}/  
  
RUN rm -rf conf/*  
COPY nginx ${NGINX_PREFIX}/  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off; error_log /dev/stderr info;"]  


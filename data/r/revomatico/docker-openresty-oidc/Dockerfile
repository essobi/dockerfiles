FROM alpine  
MAINTAINER Cristian Chiru <cristian.chiru@dcsi.eu>  
  
ENV LUA_SUFFIX=jit-2.1.0-beta3 \  
LUAJIT_VERSION=2.1 \  
NGINX_PREFIX=/opt/openresty/nginx \  
OPENRESTY_PREFIX=/opt/openresty \  
OPENRESTY_SRC_SHA256=d1246e6cfa81098eea56fb88693e980d3e6b8752afae686fab271519b81d696b
\  
OPENRESTY_VERSION=1.13.6.1 \  
LUAROCKS_VERSION=2.4.1 \  
LUAROCKS_SRC_SHA256=e429e0af9764bfd5cb640cac40f9d4ed1023fa17c052dff82ed0a41c05f3dcf9
\  
VAR_PREFIX=/var/nginx  
  
RUN set -ex \  
&& apk \--no-cache add \  
libgcc \  
libpcrecpp \  
libpcre16 \  
libpcre32 \  
libssl1.0 \  
libstdc++ \  
openssl \  
pcre \  
curl \  
unzip \  
git \  
dnsmasq \  
&& apk \--no-cache add --virtual .build-dependencies \  
make \  
musl-dev \  
gcc \  
ncurses-dev \  
openssl-dev \  
pcre-dev \  
perl \  
readline-dev \  
zlib-dev \  
libc-dev \  
\  
## OpenResty  
&& curl -fsSL
https://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz -o
/tmp/openresty.tar.gz \  
\  
&& cd /tmp \  
&& echo "${OPENRESTY_SRC_SHA256} *openresty.tar.gz" | sha256sum -c - \  
&& tar -xzf openresty.tar.gz \  
\  
&& cd openresty-* \  
&& readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& ./configure \  
\--prefix=${OPENRESTY_PREFIX} \  
\--http-client-body-temp-path=${VAR_PREFIX}/client_body_temp \  
\--http-proxy-temp-path=${VAR_PREFIX}/proxy_temp \  
\--http-log-path=${VAR_PREFIX}/access.log \  
\--error-log-path=${VAR_PREFIX}/error.log \  
\--pid-path=${VAR_PREFIX}/nginx.pid \  
\--lock-path=${VAR_PREFIX}/nginx.lock \  
\--with-luajit \  
\--with-pcre-jit \  
\--with-ipv6 \  
\--with-http_ssl_module \  
\--without-http_ssi_module \  
\--with-http_realip_module \  
\--without-http_scgi_module \  
\--without-http_uwsgi_module \  
\--without-http_userid_module \  
-j${NPROC} \  
&& make -j${NPROC} \  
&& make install \  
\  
&& rm -rf /tmp/openresty* \  
\  
## LuaRocks  
&& curl -fsSL
https://keplerproject.github.io/luarocks/releases/luarocks-${LUAROCKS_VERSION}.tar.gz
-o /tmp/luarocks.tar.gz \  
\  
&& cd /tmp \  
&& echo "${LUAROCKS_SRC_SHA256} *luarocks.tar.gz" | sha256sum -c - \  
&& tar -xzf luarocks.tar.gz \  
\  
&& cd luarocks-* \  
&& ./configure \  
\--prefix=${OPENRESTY_PREFIX}/luajit \  
\--lua-suffix=${LUA_SUFFIX} \  
\--with-lua=${OPENRESTY_PREFIX}/luajit \  
\--with-lua-lib=${OPENRESTY_PREFIX}/luajit/lib \  
\--with-lua-
include=${OPENRESTY_PREFIX}/luajit/include/luajit-${LUAJIT_VERSION} \  
&& make build \  
&& make install \  
\  
&& rm -rf /tmp/luarocks* \  
&& rm -rf ~/.cache/luarocks \  
## Post install  
&& ln -sf ${NGINX_PREFIX}/sbin/nginx /usr/local/bin/nginx \  
&& ln -sf ${NGINX_PREFIX}/sbin/nginx /usr/local/bin/openresty \  
&& ln -sf ${OPENRESTY_PREFIX}/bin/resty /usr/local/bin/resty \  
&& ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luajit-*
${OPENRESTY_PREFIX}/luajit/bin/lua \  
&& ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luajit-* /usr/local/bin/lua \  
&& ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luarocks /usr/local/bin/luarocks \  
&& ln -sf ${OPENRESTY_PREFIX}/luajit/bin/luarocks-admin
/usr/local/bin/luarocks-admin \  
&& echo user=root >> /etc/dnsmasq.conf \  
## Install lua-resty-openidc  
&& cd ~/ \  
&& luarocks install lua-resty-openidc \  
## Cleanup  
&& apk del .build-dependencies 2>/dev/null  
  
WORKDIR $NGINX_PREFIX  
  
CMD ["openresty", "-g", "daemon off; error_log /dev/stderr info;"]  


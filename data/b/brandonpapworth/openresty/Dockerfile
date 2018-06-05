# Based off Dockerfile - Debian Jessie  
# from https://github.com/openresty/docker-
openresty/blob/1.11.2.2/jessie/Dockerfile  
  
FROM debian:jessie  
  
MAINTAINER Brandon Papworth <brandon@papworth.me>  
  
ARG RESTY_PREFIX="/usr/local/openresty"  
ARG RESTY_J="1"  
  
ENV
PATH="$PATH:$RESTY_PREFIX/nginx/sbin:$RESTY_PREFIX/bin:$RESTY_PREFIX/luajit/bin"
\  
OPENRESTY__PREFIX="$RESTY_PREFIX" \  
OPENRESTY__CUSTOM_LUA_PATH=/data/openresty/lualib \  
NGINX__PREFIX="$RESTY_PREFIX/nginx" \  
NGINX__CONF_PREFIX="$RESTY_PREFIX/nginx/conf" \  
NGINX__RUN_PREFIX=/var/run/nginx \  
NGINX__LOCK_PREFIX=/var/lock/nginx \  
NGINX__TMP_PREFIX=/var/tmp/nginx \  
NGINX__LOG_PREFIX=/var/log/nginx \  
NGINX__ERROR_LOG_LEVEL=info \  
NGINX__WORKER_CONNECTIONS=2048 \  
NGINX__WORKER_PROCESSES=1 \  
NGINX__HTTP__LOG_PATH__ACCESS=/dev/stdout \  
NGINX__HTTP__LOG_CONFIG__ACCESS="/dev/stdout combined" \  
NGINX__HTTP__LOG_PATH__ERROR=/dev/stderr \  
NGINX__RESOLVER=8.8.8.8 \  
NGINX__KEEPALIVE_TIMEOUT=65 \  
NGINX__COMPRESSION_TYPES="text/plain text/css text/javascript text/xml
application/json application/x-javascript application/graphql
application/x-graphql application/xml application/xml+rss application/x-www-
form-urlencoded application/vnd.ms-fontobject application/x-font-ttf
font/opentype image/svg+xml image/x-icon" \  
NGINX__BROTLI=on \  
NGINX__BROTLI_STATIC=off \  
NGINX__BROTLI_COMP_LEVEL=6 \  
NGINX__BROTLI_WINDOW=512k \  
NGINX__BROTLI_MIN_LENGTH=20  
  
ENV NGINX__PID_PATH="$NGINX__RUN_PREFIX/nginx.pid" \  
NGINX__LOCK_PATH="$NGINX__LOCK_PREFIX/nginx.lock" \  
NGINX__ERROR_LOG__CONF_FILE_PATH="$NGINX__CONF_PREFIX/error_log.conf" \  
NGINX__WORKER_CONNECTIONS__CONF_FILE_PATH="$NGINX__CONF_PREFIX/worker_connections.conf"
\  
NGINX__WORKER_PROCESSES__CONF_FILE_PATH="$NGINX__CONF_PREFIX/worker_processes.conf"
\  
NGINX__HTTP__LOG_CONFIG__ACCESS__CONF_FILE_PATH="$NGINX__CONF_PREFIX/access_log_http.conf"
\  
NGINX__HTTP__PROXY__TEMP_PATH="$NGINX__TMP_PREFIX/tmp_proxy" \  
NGINX__HTTP__CLIENT_BODY__TEMP_PATH="$NGINX__TMP_PREFIX/tmp_client_body" \  
NGINX__FCGI__PROXY__TEMP_PATH="$NGINX__TMP_PREFIX/tmp_fcgi" \  
NGINX__ENV__CONF_FILE_PATH="$NGINX__CONF_PREFIX/env_vars_available.conf" \  
NGINX__ENV__LUA_FILE_PATH="$OPENRESTY__PREFIX/lualib/generated/env_vars_available.lua"
\  
NGINX__RESOLVER__CONF_FILE_PATH="$NGINX__CONF_PREFIX/resolver.conf" \  
NGINX__KEEPALIVE_TIMEOUT__CONF_FILE_PATH="$NGINX__CONF_PREFIX/keepalive_timeout.conf"
\  
NGINX__GZIP_TYPES__CONF_FILE_PATH="$NGINX__CONF_PREFIX/gzip_types.conf" \  
NGINX__BROTLI__CONF_FILE_PATH="$NGINX__CONF_PREFIX/brotli.conf" \  
NGINX__BROTLI_STATIC__CONF_FILE_PATH="$NGINX__CONF_PREFIX/brotli_static.conf"
\  
NGINX__BROTLI_COMP_LEVEL__CONF_FILE_PATH="$NGINX__CONF_PREFIX/brotli_comp_level.conf"
\  
NGINX__BROTLI_WINDOW__CONF_FILE_PATH="$NGINX__CONF_PREFIX/brotli_window.conf"
\  
NGINX__BROTLI_MIN_LENGTH__CONF_FILE_PATH="$NGINX__CONF_PREFIX/brotli_min_length.conf"
\  
NGINX__BROTLI_TYPES__CONF_FILE_PATH="$NGINX__CONF_PREFIX/brotli_types.conf"  
  
WORKDIR $NGINX__PREFIX/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["nginx"]  
  
ARG RESTY_VERSION="1.11.2.2"  
ARG RESTY_LUAROCKS_VERSION="2.3.0"  
ARG RESTY_OPENSSL_VERSION="1.0.2j"  
ARG RESTY_PCRE_VERSION="8.39"  
  
LABEL org.openresty.version="1.11.2.2" \  
org.nginx.version="1.11.2" \  
org.luarocks.version="2.3.0"  
  
ARG _RESTY_CONFIG_DEPS="\  
\--with-openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION} \  
\--with-pcre=/tmp/pcre-${RESTY_PCRE_VERSION} \  
\--add-module=/tmp/ngx_brotli \  
\--http-client-body-temp-path=${NGINX__HTTP__CLIENT_BODY__TEMP_PATH} \  
\--http-fastcgi-temp-path=${NGINX__FCGI__PROXY__TEMP_PATH} \  
\--http-proxy-temp-path=${NGINX__HTTP__PROXY__TEMP_PATH} \  
\--http-log-path=${NGINX__HTTP__LOG_PATH__ACCESS} \  
\--error-log-path=${NGINX__HTTP__LOG_PATH__ERROR} \  
\--pid-path=${NGINX__PID_PATH} \  
\--lock-path=${NGINX__LOCK_PATH} \  
-j${RESTY_J}"  
ARG RESTY_CONFIG_OPTIONS="\  
\--with-file-aio \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_geoip_module=dynamic \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module=dynamic \  
\--with-http_mp4_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_xslt_module=dynamic \  
\--with-ipv6 \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-md5-asm \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-threads \  
"  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
libgd-dev \  
libgeoip-dev \  
libncurses5-dev \  
libperl-dev \  
libreadline-dev \  
libxslt1-dev \  
make \  
perl \  
unzip \  
zlib1g-dev \  
git \  
libtool \  
autoconf \  
automake \  
autotools-dev \  
&& cd /tmp \  
&& git clone https://github.com/google/ngx_brotli \  
&& cd /tmp/ngx_brotli \  
&& git submodule update --init \  
&& cd /tmp \  
&& git clone https://github.com/bagder/libbrotli \  
&& cd /tmp/libbrotli \  
&& git submodule update --init \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& cd /tmp \  
&& rm -rf /tmp/libbrotli \  
&& curl -fSL
https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& curl -fSL
https://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz
-o pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& curl -fSL https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz
-o openresty-${RESTY_VERSION}.tar.gz \  
&& tar xzf openresty-${RESTY_VERSION}.tar.gz \  
&& cd /tmp/openresty-${RESTY_VERSION} \  
&& ./configure ${_RESTY_CONFIG_DEPS} ${RESTY_CONFIG_OPTIONS} \  
&& make \  
&& make install \  
&& mkdir -p $OPENRESTY__PREFIX/lualib/util \  
&& mkdir -p $OPENRESTY__PREFIX/lualib/generated \  
&& mkdir -p $OPENRESTY__CUSTOM_LUA_PATH \  
&& cd /tmp \  
&& rm -rf \  
openssl-${RESTY_OPENSSL_VERSION} \  
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
openresty-${RESTY_VERSION}.tar.gz openresty-${RESTY_VERSION} \  
pcre-${RESTY_PCRE_VERSION}.tar.gz pcre-${RESTY_PCRE_VERSION} \  
&& curl -fSL
http://luarocks.org/releases/luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz -o
luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& tar xzf luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& cd luarocks-${RESTY_LUAROCKS_VERSION} \  
&& ./configure \  
\--prefix=/usr/local/openresty/luajit \  
\--with-lua=/usr/local/openresty/luajit \  
\--lua-suffix=jit-2.1.0-beta2 \  
\--with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1 \  
&& make build \  
&& make install \  
&& cd /tmp \  
&& rm -rf luarocks-${RESTY_LUAROCKS_VERSION}
luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& DEBIAN_FRONTEND=noninteractive apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
VOLUME ["/var/run/nginx", "/var/lock/nginx", "/var/tmp/nginx",
"/var/log/nginx"]  
  
RUN echo "docker-build-script: Downloading and installing LuaRocks includes" \  
&& luarocks install lua-resty-template \  
&& luarocks install lua-resty-validation \  
&& luarocks install lua-resty-uuid \  
&& luarocks install lua-resty-reqargs \  
&& luarocks install lua-resty-session \  
&& luarocks install lua-resty-http  
  
COPY artifacts/env.lua $OPENRESTY__PREFIX/lualib/util/env.lua  
COPY artifacts/nginx.conf $NGINX__PREFIX/conf/nginx.conf  
COPY artifacts/default.conf $NGINX__PREFIX/conf/sites_enabled/default.conf  
  
COPY ["artifacts/docker-entrypoint.sh", "/"]  
COPY ["artifacts/docker-entrypoint-scripts", "/docker-entrypoint-scripts"]  


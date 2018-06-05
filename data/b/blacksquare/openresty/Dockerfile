FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV OPENRESTY_VERSION 1.9.3.1  
ENV OPENRESTY_PREFIX /opt/openresty  
ENV NGINX_PREFIX /opt/openresty/nginx  
ENV VAR_PREFIX /var/nginx  
  
RUN apt-get update && apt-get install -y libpcre3 libssl1.0.0 dnsmasq && rm
-rf /var/lib/apt/lists/*  
  
RUN buildDeps='curl perl make build-essential procps libreadline-dev
libncurses5-dev libpcre3-dev libssl-dev' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SL
"http://openresty.org/download/ngx_openresty-${OPENRESTY_VERSION}.tar.gz" -o
openresty.tar.gz \  
&& mkdir -p /usr/src/openresty \  
&& tar -xzf openresty.tar.gz -C /usr/src/openresty --strip-components=1 \  
&& rm openresty.tar.gz \  
&& cd /usr/src/openresty \  
&& readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& ./configure \  
\--prefix=$OPENRESTY_PREFIX \  
\--http-client-body-temp-path=$VAR_PREFIX/client_body_temp \  
\--http-proxy-temp-path=$VAR_PREFIX/proxy_temp \  
\--http-log-path=$VAR_PREFIX/access.log \  
\--error-log-path=$VAR_PREFIX/error.log \  
\--pid-path=$VAR_PREFIX/nginx.pid \  
\--lock-path=$VAR_PREFIX/nginx.lock \  
\--with-luajit \  
\--with-http_gzip_static_module \  
\--with-http_realip_module \  
\--with-http_stub_status_module \  
\--with-http_ssl_module \  
\--with-http_sub_module \  
\--with-http_spdy_module \  
\--without-http_fastcgi_module \  
\--without-http_scgi_module \  
\--without-http_uwsgi_module \  
\--with-http_stub_status_module \  
\--with-http_secure_link_module \  
\--with-http_sub_module \  
\--with-ipv6 \  
\--with-pcre-jit \  
\--with-sha1=/usr/include/openssl \  
\--with-md5=/usr/include/openssl \  
\--without-lua_resty_mysql \  
\--without-lua_resty_websocket \  
-j${NPROC} \  
&& make -j${NPROC} \  
&& make install \  
&& ln -sf $NGINX_PREFIX/sbin/nginx /usr/local/bin/nginx \  
&& ln -sf $NGINX_PREFIX/sbin/nginx /usr/local/bin/openresty \  
&& ln -sf $OPENRESTY_PREFIX/bin/resty /usr/local/bin/resty \  
&& ln -sf $OPENRESTY_PREFIX/luajit/bin/luajit-*
$OPENRESTY_PREFIX/luajit/bin/lua \  
&& ln -sf $OPENRESTY_PREFIX/luajit/bin/luajit-* /usr/local/bin/lua \  
&& cd / && rm -rf /usr/src/openresty \  
&& apt-get purge -y --auto-remove $buildDeps  
  
CMD ["nginx", "-g", "daemon off; error_log /dev/stderr info;"]  


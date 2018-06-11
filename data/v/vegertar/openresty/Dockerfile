FROM debian:wheezy  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl perl make build-essential procps \  
libreadline-dev libncurses5-dev libpcre3-dev libssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV OPENRESTY_VERSION 1.9.7.4  
ENV VAR_PREFIX /var/nginx  
ENV LUAROCKS_VERSION 2.3.0  
ENV ROOT /root  
  
# NginX prefix is automatically set by OpenResty to $OPENRESTY_PREFIX/nginx  
# look for $ngx_prefix in
https://github.com/openresty/ngx_openresty/blob/master/util/configure  
RUN cd $ROOT \  
&& echo "==> Downloading OpenResty..." \  
&& curl -sSL
http://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz | tar -xvz
\  
&& echo "==> Configuring OpenResty..." \  
&& cd openresty-* \  
&& readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& echo "using upto $NPROC threads" \  
&& ./configure \  
\--http-client-body-temp-path=$VAR_PREFIX/client_body_temp \  
\--http-proxy-temp-path=$VAR_PREFIX/proxy_temp \  
\--http-log-path=$VAR_PREFIX/access.log \  
\--error-log-path=$VAR_PREFIX/error.log \  
\--pid-path=$VAR_PREFIX/nginx.pid \  
\--lock-path=$VAR_PREFIX/nginx.lock \  
\--with-luajit \  
\--with-pcre-jit \  
\--with-file-aio \  
\--with-ipv6 \  
\--with-http_stub_status_module \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_gunzip_module \  
\--with-stream \  
-j${NPROC} \  
&& echo "==> Building OpenResty..." \  
&& make -j${NPROC} \  
&& echo "==> Installing OpenResty..." \  
&& make install \  
&& echo "==> Finishing..." \  
&& rm -rf $ROOT/ngx_openresty*  
  
RUN cd $ROOT \  
&& echo "==> Downloading LuaRocks..." \  
&& curl -sSL http://luarocks.org/releases/luarocks-${LUAROCKS_VERSION}.tar.gz
| tar -xvz \  
&& echo "==> Configuring LuaRocks..." \  
&& cd luarocks-* \  
&& ./configure \  
\--prefix=/usr/local/openresty/luajit \  
\--with-lua=/usr/local/openresty/luajit \  
\--lua-suffix=jit-2.1.0-beta1 \  
\--with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1 \  
&& echo "==> Installing LuaRocks..." \  
&& make \  
&& echo "==> Installing LuaRocks..." \  
&& make install \  
&& echo "==> Finishing..." \  
&& rm -rf $ROOT/luarocks*


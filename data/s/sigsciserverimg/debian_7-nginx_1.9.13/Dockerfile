  
FROM debian:7  
MAINTAINER info@signalsciences.com  
  
LABEL com.signalsciences.base-os_name=debian \  
com.signalsciences.base-os_version=7 \  
com.signalsciences.base-server_name=nginx \  
com.signalsciences.base-server_version=1.9.13  
  
ENV NGINX_VERSION=1.9.13 \  
NGINX_LUA=0.10.2 \  
NGINX_DEVEL=0.2.19 \  
LUAJIT=2.0.4  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates wget make procps
\  
&& export INSTALL_PACKAGES="gcc autoconf automake libtool libc6-dev libc-dev
libpcre3-dev zlib1g-dev libssl-dev pgp" \  
&& apt-get install -yy --no-install-recommends \  
libpcre3 zlib1g openssl \  
${INSTALL_PACKAGES} \  
&& cd /root \  
&& wget -nv -O LuaJIT-${LUAJIT}.tar.gz
http://luajit.org/download/LuaJIT-${LUAJIT}.tar.gz \  
&& wget -nv -O nginx-${NGINX_VERSION}.tar.gz
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& wget -nv -O lua-nginx-module-${NGINX_LUA}.tar.gz
https://github.com/openresty/lua-nginx-module/archive/v${NGINX_LUA}.tar.gz \  
&& wget -nv -O ngx_devel_kit-${NGINX_DEVEL}.tar.gz
https://github.com/simpl/ngx_devel_kit/archive/v${NGINX_DEVEL}.tar.gz \  
&& tar -xf LuaJIT-${LUAJIT}.tar.gz \  
&& tar -xf lua-nginx-module-${NGINX_LUA}.tar.gz \  
&& tar -xf ngx_devel_kit-${NGINX_DEVEL}.tar.gz \  
&& tar -xf nginx-${NGINX_VERSION}.tar.gz \  
&& cd LuaJIT-${LUAJIT} \  
&& make amalg PREFIX=/usr \  
&& make install PREFIX=/usr \  
&& ldconfig \  
&& cd /root/nginx-${NGINX_VERSION} \  
&& ./configure \  
\--with-http_realip_module \  
\--with-http_ssl_module \  
\--add-module=/root/ngx_devel_kit-${NGINX_DEVEL} \  
\--add-module=/root/lua-nginx-module-${NGINX_LUA} \  
&& make \  
&& make install \  
&& cd /root \  
&& rm -rf nginx* LuaJIT* lua-nginx-module-* ngx_devel_kit-* \  
&& apt-get purge -y ${INSTALL_PACKAGES} \  
&& apt-get autoremove -y \  
&& apt-get clean  


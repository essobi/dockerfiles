  
FROM centos:5  
MAINTAINER info@signalsciences.com  
  
LABEL com.signalsciences.base-os_name=centos \  
com.signalsciences.base-os_version=5 \  
com.signalsciences.base-server_name=nginx \  
com.signalsciences.base-server_version=1.9.13  
  
ENV NGINX_VERSION=1.9.13 \  
NGINX_LUA=0.10.2 \  
NGINX_DEVEL=0.2.19 \  
LUAJIT=2.0.4  
  
  
  
  
RUN set -ex \  
&& yum install -y make wget curl \  
&& export INSTALL_PACKAGES="gcc autoconf automake libtool pcre-devel openssl-
devel" \  
&& yum install -y ${INSTALL_PACKAGES} pcre openssl \  
&& cd /root \  
&& curl -L --silent --output LuaJIT-${LUAJIT}.tar.gz
http://luajit.org/download/LuaJIT-${LUAJIT}.tar.gz \  
&& curl -L --silent --output nginx-${NGINX_VERSION}.tar.gz
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& curl -L --silent --output lua-nginx-module-${NGINX_LUA}.tar.gz
https://github.com/openresty/lua-nginx-module/archive/v${NGINX_LUA}.tar.gz \  
&& curl -L --silent --output ngx_devel_kit-${NGINX_DEVEL}.tar.gz
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
&& yum remove -y ${INSTALL_PACKAGES} \  
&& yum clean headers \  
&& yum clean packages \  
&& rm -rf /var/cache/yum/*  


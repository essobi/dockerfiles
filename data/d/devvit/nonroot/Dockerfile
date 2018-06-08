FROM php:fpm-alpine  
  
ARG RESTY_VER=1.13.6.2  
ARG LUAROCKS_VER=2.4.4  
ARG RESTY_DIR=/usr/local  
  
RUN apk add \--no-cache \--update bash build-base curl unzip git gd grep
mariadb mariadb-client sphinx libxslt-dev libressl-dev ruby ruby-dev ruby-irb
ruby-io-console ruby-json \  
&& apk add \--no-cache \--virtual .build-deps perl pcre-dev mariadb-dev
libjpeg-turbo-dev libpng-dev \  
&& docker-php-ext-install gd mysqli opcache zip  
  
ENV
PATH=$PATH:$RESTY_DIR/openresty/bin:$RESTY_DIR/openresty/nginx/sbin:$RESTY_DIR/openresty/luajit/bin  
  
RUN cd /tmp \  
&& curl -fSL -O https://openresty.org/download/openresty-${RESTY_VER}.tar.gz \  
&& tar -xzf openresty-${RESTY_VER}.tar.gz \  
&& cd openresty-${RESTY_VER} \  
&& git clone https://github.com/vozlt/nginx-module-vts \  
&& git clone https://github.com/tg123/websockify-nginx-module \  
&& sed -ie 's/DEFAULT_ENCODE_EMPTY_TABLE_AS_OBJECT
1/DEFAULT_ENCODE_EMPTY_TABLE_AS_OBJECT 0/g' bundle/lua-cjson-*/lua_cjson.c \  
&& ./configure \--prefix=$RESTY_DIR/openresty \--with-http_realip_module
\--add-module=./nginx-module-vts \--add-module=./websockify-nginx-module \  
&& make -s -j$(nproc) install \  
&& curl -fSL -O https://luarocks.org/releases/luarocks-${LUAROCKS_VER}.tar.gz
\  
&& tar -xzf luarocks-${LUAROCKS_VER}.tar.gz \  
&& cd luarocks-${LUAROCKS_VER} \  
&& ./configure \--prefix=$RESTY_DIR/openresty/luajit \--with-lua-
include=$RESTY_DIR/openresty/luajit/include/luajit-2.1 \--lua-suffix=jit \  
&& make build \  
&& make install  
  
RUN cd /tmp \  
&& cd openresty-${RESTY_VER}/build/lua-cjson-* \  
&& luarocks make \  
&& gem install bundler foreman mysql2 \--no-ri \--no-rdoc  
  
RUN cd /tmp \  
&& apk del .build-deps \  
&& rm -rf openresty*  


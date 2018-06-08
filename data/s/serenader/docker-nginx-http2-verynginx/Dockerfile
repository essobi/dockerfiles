FROM ubuntu:14.04  
MAINTAINER serenader "xyslive@gmail.com"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
libpcre3 \  
libpcre3-dev \  
zlib1g-dev \  
unzip \  
git \  
ca-certificates \  
wget \  
curl \  
libssl-dev \  
autoconf \  
libtool \  
python \  
automake \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& groupadd nginx \  
&& useradd -d /var/cache/nginx -s /sbin/nologin -g nginx nginx  
RUN wget -O nginx-ct.zip -c https://github.com/grahamedgecombe/nginx-
ct/archive/v1.3.0.zip \  
&& unzip nginx-ct.zip \  
&& git clone https://github.com/bagder/libbrotli \  
&& cd libbrotli \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& git clone https://github.com/google/ngx_brotli.git \  
&& wget -O openssl.tar.gz -c
https://github.com/openssl/openssl/archive/OpenSSL_1_0_2j.tar.gz \  
&& tar zxf openssl.tar.gz \  
&& git clone https://github.com/travislee8964/sslconfig.git \  
&& cd openssl-OpenSSL_1_0_2j \  
&& patch -p1 <
../sslconfig/patches/openssl__chacha20_poly1305_draft_and_rfc_ossl102i.patch \  
&& cd .. \  
&& git clone https://github.com/alexazhou/VeryNginx.git \  
&& cd VeryNginx && python ./install.py install verynginx \  
&& cd .. \  
&& wget -O LuaJIT-2.1.0.tar.gz -c
http://luajit.org/download/LuaJIT-2.1.0-beta1.tar.gz \  
&& tar zxf LuaJIT-2.1.0.tar.gz \  
&& cd LuaJIT-2.1.0-beta1 \  
&& make \  
&& make install \  
&& cd .. \  
&& wget -O ngx_devel_kit.tar.gz -c
https://github.com/simpl/ngx_devel_kit/archive/v0.3.0.tar.gz \  
&& tar zxf ngx_devel_kit.tar.gz \  
&& wget -O lua_nginx_module.tar.gz -c https://github.com/openresty/lua-nginx-
module/archive/v0.10.6.tar.gz \  
&& tar zxf lua_nginx_module.tar.gz \  
&& wget -O nginx-1.11.4.tar.gz -c
https://nginx.org/download/nginx-1.11.4.tar.gz \  
&& tar zxf nginx-1.11.4.tar.gz \  
&& export LUAJIT_LIB=/usr/local/lib \  
&& export LUAJIT_INC=/usr/local/include/luajit-2.1 \  
&& cd nginx-1.11.4 \  
&& ./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
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
\--add-module=../ngx_brotli \  
\--add-module=../nginx-ct-1.3.0 \  
\--add-module=../lua-nginx-module-0.10.6 \  
\--add-module=../ngx_devel_kit-0.3.0 \  
\--with-openssl=../openssl-OpenSSL_1_0_2j \  
\--with-http_v2_module \  
\--with-http_ssl_module \  
\--with-ipv6 \  
\--with-http_gzip_static_module \  
\--with-http_realip_module \  
\--with-http_stub_status_module \  
&& make \  
&& make install \  
&& cd .. \  
&& rm nginx-ct.zip \  
&& rm openssl.tar.gz \  
&& rm LuaJIT-2.1.0.tar.gz \  
&& rm ngx_devel_kit.tar.gz \  
&& rm lua_nginx_module.tar.gz \  
&& rm nginx-1.11.4.tar.gz \  
&& rm -rf libbrotli \  
&& rm -rf ngx_brotli \  
&& rm -rf openssl-OpenSSL_1_0_2j \  
&& rm -rf VeryNginx \  
&& rm -rf LuaJIT-2.1.0-beta1 \  
&& rm -rf nginx-1.11.4 \  
&& rm -rf nginx-ct-1.3.0 \  
&& rm -rf lua-nginx-module-0.10.6 \  
&& rm -rf ngx_devel_kit-0.3.0  
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/usr_local_lib.conf && ldconfig  
COPY nginx.conf /etc/nginx/nginx.conf  
RUN apt-get purge build-essential -y \  
&& apt-get autoremove -y  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
VOLUME ["/var/cache/nginx"]  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  


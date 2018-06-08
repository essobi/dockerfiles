FROM ubuntu:trusty  
  
MAINTAINER THRON Devops <devops@thron.com>  
  
ENV NGINX_VERSION=1.12.1 \  
NGINX_DEVEL_KIT_MODULE_VERSION=0.3.0 \  
NGINX_LUA_MODULE_VERSION=0.10.9rc8 \  
NGINX_HEADERS_MORE_MODULE_VERSION=0.32 \  
NGINX_SET_MISC_MODULE_VERSION=0.31 \  
OPENSSL_VERSION=1.0.2l \  
PCRE_VERSION=8.41 \  
ZLIB_VERSION=1.2.11 \  
NGINX_PREFIX=/usr/local/nginx \  
NGINX_BIN_PATH=/sbin/nginx \  
NGINX_CONF_PATH=/etc/nginx/nginx.conf \  
NGINX_LOG_DIR=/var/log/nginx  
  
RUN apt-get update \  
&& apt-get -y -o Dpkg::Options::="--force-confdef" install \  
build-essential \  
dos2unix \  
htop \  
liblua5.1 liblua5.1-dev \  
libxslt1-dev \  
nano \  
wget  
  
WORKDIR /usr/local/src  
RUN wget -c -v http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& tar -xzf nginx-${NGINX_VERSION}.tar.gz \  
&& rm -f nginx-${NGINX_VERSION}.tar.gz \  
&& mkdir -p nginx-${NGINX_VERSION}/modules  
  
WORKDIR nginx-${NGINX_VERSION}/modules  
RUN wget -c -v -O headers-more-nginx-
module-${NGINX_HEADERS_MORE_MODULE_VERSION}.tar.gz
https://github.com/openresty/headers-more-nginx-
module/archive/v${NGINX_HEADERS_MORE_MODULE_VERSION}.tar.gz \  
&& tar zxvf headers-more-nginx-
module-${NGINX_HEADERS_MORE_MODULE_VERSION}.tar.gz \  
&& wget -c -v -O openssl-${OPENSSL_VERSION}.tar.gz
http://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \  
&& tar zxvf openssl-${OPENSSL_VERSION}.tar.gz \  
&& wget -c -v -O ngx_devel_kit-${NGINX_DEVEL_KIT_MODULE_VERSION}.tar.gz
https://github.com/simpl/ngx_devel_kit/archive/v${NGINX_DEVEL_KIT_MODULE_VERSION}.tar.gz
\  
&& tar zxvf ngx_devel_kit-${NGINX_DEVEL_KIT_MODULE_VERSION}.tar.gz \  
&& wget -c -v -O lua-nginx-module-${NGINX_LUA_MODULE_VERSION}.tar.gz
https://github.com/openresty/lua-nginx-
module/archive/v${NGINX_LUA_MODULE_VERSION}.tar.gz \  
&& tar zxvf lua-nginx-module-${NGINX_LUA_MODULE_VERSION}.tar.gz \  
&& wget -c -v http://zlib.net/zlib-${ZLIB_VERSION}.tar.gz \  
&& tar zxvf zlib-${ZLIB_VERSION}.tar.gz \  
&& wget -c -v
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${PCRE_VERSION}.tar.gz
\  
&& tar zxvf pcre-${PCRE_VERSION}.tar.gz \  
&& wget -c -v -O set-misc-nginx-module-${NGINX_SET_MISC_MODULE_VERSION}.tar.gz
https://github.com/openresty/set-misc-nginx-
module/archive/v${NGINX_SET_MISC_MODULE_VERSION}.tar.gz \  
&& tar zxvf set-misc-nginx-module-${NGINX_SET_MISC_MODULE_VERSION}.tar.gz \  
&& rm -f *.tar.gz  
  
WORKDIR ../  
RUN ./configure \  
\--sbin-path=${NGINX_BIN_PATH} \  
\--conf-path=${NGINX_CONF_PATH} \  
\--prefix=${NGINX_PREFIX} \  
\--error-log-path=${NGINX_LOG_DIR}/error.log \  
\--http-client-body-temp-path=/var/lib/nginx/body \  
\--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \  
\--http-log-path=${NGINX_LOG_DIR}/access.log \  
\--http-proxy-temp-path=/var/lib/nginx/proxy \  
\--http-scgi-temp-path=/var/lib/nginx/scgi \  
\--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \  
\--lock-path=/var/lock/nginx.lock \  
\--pid-path=/var/run/nginx.pid \  
\--without-mail_pop3_module \  
\--without-mail_imap_module \  
\--without-mail_smtp_module \  
\--with-file-aio \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_slice_module \  
\--with-http_v2_module \  
\--with-stream \  
\--add-module=modules/lua-nginx-module-${NGINX_LUA_MODULE_VERSION} \  
\--add-module=modules/ngx_devel_kit-${NGINX_DEVEL_KIT_MODULE_VERSION} \  
\--add-module=modules/headers-more-nginx-
module-${NGINX_HEADERS_MORE_MODULE_VERSION} \  
\--add-module=modules/set-misc-nginx-module-${NGINX_SET_MISC_MODULE_VERSION} \  
\--with-pcre=modules/pcre-${PCRE_VERSION} \  
\--with-zlib=modules/zlib-${ZLIB_VERSION} \  
\--with-http_ssl_module \  
\--with-openssl=modules/openssl-${OPENSSL_VERSION} \  
\--with-http_xslt_module \  
\--with-ipv6 \  
\--with-sha1=/usr/include/openssl \  
\--with-md5=/usr/include/openssl \  
\--with-http_stub_status_module \  
\--with-cc-opt=-Wno-error \  
&& make  
  
RUN cp objs/nginx /usr/sbin/nginx && chmod 755 /usr/sbin/nginx  
  
WORKDIR /home/ubuntu  
  
RUN apt-get -y -o Dpkg::Options::="--force-confdef" remove \  
build-essential \  
liblua5.1 liblua5.1-dev \  
libxslt1-dev \  
&& apt-get -y -o Dpkg::Options::="--force-confdef" install \  
jq \  
liblua5.1-0 \  
libxslt1.1 \  
logrotate \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /usr/local/src/nginx* /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  


FROM ubuntu:16.04  
  
MAINTAINER eXo Platform <docker@exoplatform.com>  
  
ENV NPS_VERSION=1.11.33.4  
ENV NPS_FULL_VERSION=1.11.33.4-beta  
ENV NPS_DIR_NAME=incubator-pagespeed-ngx-release-${NPS_FULL_VERSION}  
ENV NGINX_VERSION=1.11.10  
ENV MORE_HEADERS_VERSION=0.32  
ENV BUILD_DIR=/tmp/build  
  
RUN apt-get update && apt-get install -y build-essential zlib1g-dev libpcre3
libpcre3-dev unzip wget curl libssl-dev dnsmasq supervisor libldap2-dev git &&
\  
rm -rf /var/lib/apt/lists/*  
RUN mkdir ${BUILD_DIR} && \  
cd ${BUILD_DIR} && wget
https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_FULL_VERSION}.zip
&& \  
unzip release-${NPS_FULL_VERSION}.zip && \  
cd ${NPS_DIR_NAME} && \  
wget https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz && \  
tar -xzvf ${NPS_VERSION}.tar.gz && \  
cd ${BUILD_DIR} && \  
wget https://github.com/openresty/headers-more-nginx-
module/archive/v${MORE_HEADERS_VERSION}.tar.gz && \  
tar -xzf v${MORE_HEADERS_VERSION}.tar.gz && \  
cd ${BUILD_DIR} && git clone https://github.com/kvspb/nginx-auth-ldap.git &&
cd nginx-auth-ldap && git checkout b80942160417e95adbadb16adc41aaa19a6a00d9 &&
\  
cd ${BUILD_DIR} && wget
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar -xzf nginx-${NGINX_VERSION}.tar.gz && \  
cd ${BUILD_DIR}/nginx-${NGINX_VERSION} && \  
./configure --prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--modules-path=/usr/lib/nginx/modules \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--http-client-body-temp-path=/var/cache/nginx/client_temp \  
--with-http_ssl_module \  
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
--user=nginx --group=nginx \  
--add-module=${BUILD_DIR}/headers-more-nginx-module-${MORE_HEADERS_VERSION} \  
--add-module=${BUILD_DIR}/${NPS_DIR_NAME} \  
--add-module=${BUILD_DIR}/nginx-auth-ldap ${PS_NGX_EXTRA_FLAGS} \  
--with-file-aio \  
--with-threads \  
--with-http_addition_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_auth_request_module \  
--with-http_realip_module \  
--with-http_v2_module \  
--with-stream \  
--with-stream_ssl_module \  
--with-http_stub_status_module && \  
make -j 4 install && \  
rm -rf ${BUILD_DIR} && \  
mkdir -p /var/log/nginx /var/cache/nginx/ && \  
ln -s /dev/stdout /var/log/nginx/access.log && \  
ln -s /dev/sterr /var/log/nginx/error.log && \  
useradd --create-home --user-group -u 999 --shell /bin/nologin nginx  
  
COPY nginx.conf /etc/nginx/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY dnsmasq.conf /etc/dnsmasq.conf  
  
CMD ["/usr/bin/supervisord"]  


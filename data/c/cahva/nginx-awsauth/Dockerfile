FROM alpine:3.6  
  
MAINTAINER Markku Virtanen  
  
ENV NGINX_VERSION nginx-1.13.4  
  
RUN apk --update add openssl-dev git pcre-dev zlib-dev tini wget build-base &&
\  
mkdir -p /tmp/src && \  
cd /tmp/src && \  
wget http://nginx.org/download/${NGINX_VERSION}.tar.gz && \  
tar -zxvf ${NGINX_VERSION}.tar.gz && \  
cd /tmp/src/${NGINX_VERSION} && \  
git clone -b AuthV2 https://github.com/anomalizer/ngx_aws_auth.git && \  
./configure \  
--with-http_ssl_module \  
--with-http_gzip_static_module \  
--add-module=ngx_aws_auth \  
--prefix=/etc/nginx \  
--http-log-path=/var/log/nginx/access.log \  
--error-log-path=/var/log/nginx/error.log \  
--sbin-path=/usr/local/sbin/nginx && \  
make && \  
make install && \  
apk del build-base && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*


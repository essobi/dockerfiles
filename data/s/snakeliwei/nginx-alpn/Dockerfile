FROM debian:jessie  
  
MAINTAINER Lyndon "snakeliwei@gmail.com"  
  
ENV NGINX_VERSION 1.11.2  
ENV OPENSSL_VERSION 1_0_2h  
ENV NGINXCT_VERSION 1.2.0  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y ca-
certificates gcc make vim libpcre3 libpcre3-dev zlib1g-dev unzip git wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /src && \  
groupadd nginx && \  
useradd -g nginx -d /var/cache/nginx -s /sbin/nologin -m nginx && \  
cd /src && \  
wget -O openssl.zip -c
https://github.com/openssl/openssl/archive/OpenSSL_$OPENSSL_VERSION.zip && \  
unzip openssl.zip && \  
mv openssl-OpenSSL_1_0_2h/ openssl && \  
wget -O nginx-ct.zip -c https://github.com/grahamedgecombe/nginx-
ct/archive/v$NGINXCT_VERSION.zip && \  
unzip nginx-ct.zip && \  
wget -c https://nginx.org/download/nginx-1.11.2.tar.gz && \  
tar zxf nginx-1.11.2.tar.gz && \  
cd nginx-1.11.2/ && \  
./configure --prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--modules-path=/usr/lib/nginx/modules \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--user=nginx \  
--group=nginx \  
--add-module=../nginx-ct-1.2.0 \  
--with-openssl=../openssl \  
--with-http_v2_module \  
--with-http_ssl_module \  
--with-ipv6 \  
--with-http_gzip_static_module && \  
make && \  
make install && \  
rm -rf /etc/nginx/html/ && \  
mkdir /etc/nginx/conf.d/ && \  
rm -rf /src  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

